#!/usr/bin/python3

import socket
import signal
import sys
import os

sock = socket.socket()

def main():
	
	if len(sys.argv) > 2 and str(sys.argv[1]) != __file__:
		
		try:
			sock.connect((str(sys.argv[1]), 7575))
		except:
			print("[\033[0;31m-\033[0m] Error in connecting to the server...")
			sys.exit(1)
		
		signal.signal(signal.SIGINT, ctrlC)

		download()

	else:
		print("Usage: client.py SERVER_IP_ADDRESS FILENAME")

def download():
	
	global fileObj

	print("[\033[0;32m+\033[0m] Downloading the file...")

	try:
		
		fileObj = open("./" + str(sys.argv[2]), 'wb')

	except:

		print("[\033[0;31m-\033[0m] Error in writing the file...")

	p = sock.recv(4096)

	while p:
		fileObj.write(p)
		p = sock.recv(4096)

	fileObj.close()
	sock.close()

	print("[\033[0;32m+\033[0m] Download completed!")

	sys.exit(0)

def ctrlC(sig, frame):
	
	ans = input("Do you want to cancel the downloading file? [y,N]> ")

	if str(ans).lower() == 'y':
		
		# Cancel the downloading

		os.remove("./" + str(sys.argv[2]))

if __name__ == '__main__':
	main()
