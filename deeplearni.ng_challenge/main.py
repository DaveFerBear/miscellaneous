import app.server as server
import sys

DEFAULT_PORT = '5000'
DATA_FILE_LOCATION = 'data/data.txt'

if __name__ == '__main__':
	if len(sys.argv) > 2:
		raise ValueError('Too many command line arguments!')

	port = sys.argv[1] if len(sys.argv)==2 else DEFAULT_PORT
	server.start(port, DATA_FILE_LOCATION)
	
	