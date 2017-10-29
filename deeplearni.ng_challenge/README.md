# Palindrome Web Server
This REST service is written in Python and uses [Flask](http://flask.pocoo.org/) and [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/).

### How to Build
1. Install the necessary python packages: `pip install requirements.txt`
2. Run the server: `python main.py XXXX`, where XXXX is an optional param specifying port number.  Default is 5000.

### Test and Verification
A test suite can be executed by running the `test.py` script.

### Endpoint Documentation
`GET:/palindromes` - Returns a list of all the values that are palindromes, one per line.

`GET:/palindromes/count` - Returns the sum of the number of lines containing palindromes.

### File Details
* `main.py` is a starting point for execution.
* `server.py` contains server logic and endpoint declarations.
* `palindrome.py` is an extensible library for reading palindrome files.