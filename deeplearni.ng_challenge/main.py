from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Palindrome(Resource):
	def get(self):
		return {'test': 'result'}

class Palindrome_Count(Resource):
	def get(self):
		return 5

api.add_resource(Palindrome, '/palindromes')
api.add_resource(Palindrome_Count, '/palindromes/count')

if __name__ == '__main__':
     app.run(port='5000')