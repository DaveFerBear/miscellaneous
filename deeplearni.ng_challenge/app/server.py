from flask import Flask
from flask_restful import Api, Resource
from palindrome import Palindrome

app = Flask(__name__)
api = Api(app)

class PalindromeResource(Resource):
	def get(self):
		return {'test': 'result'}

class PalindromeCountResource(Resource):
	def get(self):
		return Palindrome.get_number_palindromes()

api.add_resource(PalindromeResource, '/palindromes')
api.add_resource(PalindromeCountResource, '/palindromes/count')

if __name__ == '__main__':
     app.run(port='5000')