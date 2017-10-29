from palindrome import Palindrome
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
data_file = ''

class PalindromeResource(Resource):
	def get(self):
		return ', '.join(Palindrome.get_palindrome_list(data_file))

class PalindromeCountResource(Resource):
	def get(self):
		return Palindrome.get_num_palindromes(data_file)

def start(port, data_file_name):
	data_file = data_file_name
	api.add_resource(PalindromeResource, '/palindromes')
	api.add_resource(PalindromeCountResource, '/palindromes/count')
	app.run(port=port)

