1> Basic chatbot using Python, Gradio and OpenAI's gpt-3.5-turbo LLM
2> Chatbot script has logic to capture intents (order and product) from user prompt, extract entity (order number and product name) from user prompt.
3> Webhook to extract details for the entity from .csv files and send the details to chatbot script
4> Chatbot script formats & sends the details received from webhook to LLM as a 'system' role to augment the response.
5> Created 'about' info of a fictitious eRetailer SuperMart. Created jsonl file for it and submitted it to fine tune gpt-3.5-turbo : 
   jsonl file is validated successfully but fine tuning job is failing with message 'Unable to extract tag using discriminator 'role''. 
   Have created topic in OpenAI community forum for help, waiting for response.
6> Created a faq file. Plan to create jsonl file from it and submit it for finetuning after resolving the fine tuning error from above step.
