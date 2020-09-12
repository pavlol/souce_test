import requests 
import time
import argparse
import sys

# usage example
# python3 task.py -l server.log -u http://localhost:12345/


parser = argparse.ArgumentParser(description="Souce Lab server.py error logger")
parser.add_argument("-l", "--logfile", help="Enter log file name")
parser.add_argument("-u", "--url", help="URL of the server to monitor, eg. http://localhost:12345/")
options = parser.parse_args(sys.argv[1:])
log_file = options.logfile
server_url = options.url


def log_error(text):
	print("logging")
	with open(log_file, "a") as logfile:
		logfile.write(text + "\n")

while True:
	r = requests.get(url = server_url, params = {})
	print(r.status_code)
	if(r.status_code != 200):
		log_error(r.text)
	else:
		print(r.text)
	time.sleep(1)


