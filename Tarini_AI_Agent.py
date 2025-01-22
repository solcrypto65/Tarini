import gradio as gr
from openai import OpenAI, OpenAIError
import os
from IPython.display import display, Markdown, Latex, HTML, JSON
import pandas as pd
import requests
import json
import re

messages = [
	{'role' : 'system', 'content' : 'You are an AI enabled Agent for an eRetailer SuperMart who specializing in mobile sales.'}
]


css = """
	.chatHistory {background-color: #E2EAF4 color: black}
	.promptBox {background-color: #E7DDFF, color: black !important}
	.gradio-container {background: #494545}
"""
def get_order_details(ord_number):
	webhook_url = 'http://127.0.0.1:5000/webhook'
	data = {'intent': 'orders',
			'parm': ord_number}
	response = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
	response_dict = json.loads(response.text)
	prod = str(response_dict['Product'])
	ord_date = str(response_dict['Order_Date'])
	del_date = str(response_dict['Delivery_Date'])
	sys_prompt = 'we have processed the order. please use these order details in your reply '+prod+' ordered on '+ord_date+' expected to deliver on '+del_date
	return sys_prompt

def get_product_details(product):
	webhook_url = 'http://127.0.0.1:5000/webhook'
	data = {'intent': 'products',
			'parm': product}
	response = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
	response_dict = json.loads(response.text)
	prod = str(response_dict['Product'])
	notes = str(response_dict['Notes'])
	sys_prompt = 'please use these product details in your reply '+prod+' '+notes
	return sys_prompt

def gptResponse(prompt: str):

	if 'order' in prompt:
		match_obj = re.search(r"\d{5}",prompt)
		if match_obj:
			sys_prompt = get_order_details(match_obj.group())
		else:
			sys_prompt = 'plese inform user that this is invalid order number'
		messages.append({'role' : 'system', 'content' : sys_prompt})

	if 'product' or 'mobile' or 'cellphone' in prompt:
		match_obj = re.search(r"\bproduct\s+(.*)$", prompt)
		if match_obj:
			sys_prompt = get_product_details(match_obj.group())
		else:
			sys_prompt = 'plese inform user that this product is not in stock'
		messages.append({'role' : 'system', 'content' : sys_prompt})

	messages.append({'role' : 'user', 'content' : prompt})

	resp = get_completion(messages)
	messages.append({'role' : 'assistant', 'content' : resp})

	displayMessage = ''
	for item in messages:
		if item['role'] != 'system':
			displayMessage += item['role'] + ' : ' + item['content'] + '\n\n'

	return displayMessage

def main():
	
	OpenAI.api_key  = 'API-KEY'

	with gr.Blocks(css=css) as demo:
		gr.Markdown(
			"""
				!!! Hi, Welcome to SuperMart. I am here to help you with your queries related to your orders. !!!
			""")
		with gr.Row(equal_height=True):
			prompt = gr.Textbox(label='How may I help you ?', elem_classes='promptBox', min_width=400, scale=1)
			qryBtn = gr.Button('Ask', elem_classes='promptBox', scale=0)
		output = gr.Textbox(label='Dialog History', elem_classes='chatHistory')
		qryBtn.click(fn=gptResponse, inputs=prompt, outputs=output, api_name='ask')

	demo.launch()

	messages.append({'role' : 'assistant', 'content' : resp})

	resp = get_completion(messages)
	messages.append({'role' : 'assistant', 'content' : resp})



def get_completion(messages, model="gpt-3.5-turbo", temperature=0):
    
    client = OpenAI()

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content
    except OpenAIError as e:
        return f"Error: {e}"

if __name__== "__main__":
   main()

