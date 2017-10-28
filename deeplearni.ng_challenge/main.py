from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Palindromes(Resource):
	def get(self):
		return {'test': 'result'}
class Palindrome_Count
api.add_resource(Palindromes, '/palindromes')
api.add_resource(Palindromes, '')

if __name__ == '__main__':
     app.run(port='5000')