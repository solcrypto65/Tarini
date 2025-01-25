1> Basic chatbot using Python, Gradio and OpenAI's gpt-3.5-turbo LLM
2> Chatbot script has logic to capture intents (order and product) from user prompt, extract entity (order number and product name) from user prompt.
3> Webhook to extract details for the entity from .csv files and send the details to chatbot script
4> Chatbot script formats & sends the details received from webhook to LLM as a 'system' role to augment the response.
5> Created 'about' info of a fictitious eRetailer SuperMart. Created jsonl file for it and fine tuned gpt-3.5-turbo creating a fine tuned version of LLM
6> <wip> Create a faq file. Using RAG to augment LLM's response from faq database
