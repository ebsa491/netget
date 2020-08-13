#!/usr/bin/python3

import socket
import signal
import sys

sock = socket.socket()

def main():

	global fileObj

	if len(sys.argv) > 1:
	
		try:

			fileObj = open(str(sys.argv[1]), 'rb')

		except:
			print("[\033[0;31m-\033[0m] Error in loading the file...")
			sys.exit(1)

		sock.bind(('', 7575))

		sock.listen(1)

		print("[\033[0;32m+\033[0m] Server is running...")
		
		signal.signal(signal.SIGINT, ctrlC)

		listen()

	else:
		print("Usage: server.py FILENAME")

def listen():
	
	i = 0

	while True:
		
		sc, address = sock.accept()

		print("[\033[0;32m+\033[0m] New client : " + str(address[0]))

		ans = input("Do you want to send the file? [Y,n]> ")

		if str(ans).lower() != 'n':
			
			# Send the file
			
			print("[\033[0;32m+\033[0m] Sending the file...")

			p = fileObj.read(4096)

			while p:
				sc.send(p)

				p = fileObj.read(4096)

			print("[\033[0;32m+\033[0m] Done!")

		else:
			sc.close()

	fileObj.close()
	sc.close()

def ctrlC(sig, frame):

	print("\n[\033[0;31m-\033[0m] Server is going to down...")

	fileObj.close()

	sock.close()

	sys.exit(0)

if __name__ == '__main__':
	main()
