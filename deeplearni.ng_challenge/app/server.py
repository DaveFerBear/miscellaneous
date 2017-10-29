from palindrome import Palindrome
from flask import Flask
from flask.json import jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

data_file = 'data/data.txt'


def start(port, data_file_name):
	api.add_resource(PalindromeResource, '/palindromes')
	api.add_resource(PalindromeCountResource, '/palindromes/count')
	app.run(port=port)

class PalindromeResource(Resource):
	def get(self):
		return jsonify(palindromes=Palindrome.get_palindrome_list(data_file))

class PalindromeCountResource(Resource):
	def get(self):
		return jsonify(number_palindromes=Palindrome.get_num_palindromes(data_file))
