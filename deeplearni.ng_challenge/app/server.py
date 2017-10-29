from flask import Flask
from flask_restful import Api, Resource
from palindrome import Palindrome
import sys

app = Flask(__name__)
api = Api(app)
DEFAULT_PORT = '5000'

class PalindromeResource(Resource):
	def get(self):
		return '	'.join(Palindrome.get_palindrome_list())

class PalindromeCountResource(Resource):
	def get(self):
		return Palindrome.get_num_palindromes()

api.add_resource(PalindromeResource, '/palindromes')
api.add_resource(PalindromeCountResource, '/palindromes/count')

if __name__ == '__main__':
	p = '5000'
	if len(sys.argv) > 2:
		raise ValueError('Too many command line arguments!')

	p = sys.argv[1] if len(sys.argv)==2 else DEFAULT_PORT
	app.run(port=p)