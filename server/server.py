import os
import json
from chatbot_train import chat_bot_train
from chatbot import generate_response
from flask import Flask , request
from flask_cors import CORS
import warnings

with warnings.catch_warnings():
	warnings.filterwarnings("ignore",category=FutureWarning)
	warnings.filterwarnings("ignore",category=DeprecationWarning)
	import imp

app = Flask(__name__)
cors = CORS(app, resources = {r"/*": {"origins": "*"}})
@app.route( "/getreply", methods=['POST'])
def apicall():
	test_json = request.get_json(force = True)
	print()
	print("Response Recieved")

	print()
	print(test_json)
	response = None
	if(test_json['purpose'] == 'train'):
		response = chat_bot_train()
	elif(test_json['purpose'] == 'query'):
		response = generate_response(test_json['message'])

	X = json.dumps(response)
	
	print()
	print("Sending Back ChatBot's Response")
	print("*******************************")
	return X