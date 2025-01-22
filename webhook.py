from flask import Flask, request, abort, jsonify
import pandas as pd
import os
import json

app = Flask(__name__)

@app.route("/")
def hello_world():


@app.route('/webhook', methods=['POST'])
def get_webhook():

    req = request.get_json(silent=True, force=True)

    def fetchIntentData(intent: str, parm: str):
    
        if intent == 'faq':
            df = pd.read_csv('faq.csv')
            return df.to_dict()
        elif intent == 'orders':
            df = pd.read_csv('orders.csv')
            ord_details_df = df[df['Orderid'] == eval(parm)]
            return ord_details_df.to_dict(orient='list')
        elif intent == 'products':
            df = pd.read_csv('products.csv')
            prd_details_df = df[df['Product'] == parm]
            return prd_details_df.to_dict(orient='list')

    res = fetchIntentData(req['intent'],req['parm'])

    if request.method == 'POST':
        return jsonify(res), 200
    else:
        abort(400)

if __name__ == '__main__':

  app.run()
