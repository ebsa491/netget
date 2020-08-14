#!/usr/bin/python3
# License : GPL v3.0
# Created by Saman Ebrahimnezhad .

import socket
import signal
import sys

sock = socket.socket()

def main():

	global fileObj

	if len(sys.argv) > 1 and str(sys.argv[1]) != __file__:
	
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
	
	while True:
		
		sc, address = sock.accept()

		fileObj.seek(0)

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

		sc.close()

def ctrlC(sig, frame):

	ans = input("Do you want to shutdown the server? [y,N]> ")

	if str(ans).lower() == 'y':
		
		print("\n[\033[0;31m-\033[0m] Server is going down...")

		fileObj.close()

		sock.close()

		sys.exit(0)

	else:
		print("[\033[0;32m+\033[0m] Server is up...")

if __name__ == '__main__':
	main()
