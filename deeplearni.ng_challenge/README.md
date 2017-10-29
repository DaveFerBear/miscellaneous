# Palindrome Web Server
This REST service is written in Python and uses [Flask](http://flask.pocoo.org/) and [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/).

### How to Build
1. Install the necessary python packages: `pip install requirements.txt`
2. Run the server: `python app/server.py`.  The default port is 5000, but can be changed by adding the port as an optional parameter : `python app/server.py XXXX`

### Test and Verification
A test suite can be executed by running the `test.py` script.

### Endpoint Documentation
`GET:/palindromes`

Returns a list of all the values that are palindromes, one per line.


`GET:/palindromes/count`

Returns the sum of the number of lines containing palindromes.