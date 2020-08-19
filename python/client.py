#!/usr/bin/python3
# License : GPL v3.0
# Created by Saman Ebrahimnezhad .

import socket
import signal
import sys
import os

class NetgetClient:
	def __init__(self):

		if len(sys.argv) > 2 and str(sys.argv[1]) != __file__:

			try:

				self.sock = socket.socket()
				self.sock.connect((str(sys.argv[1]), 7575))

			except:
				print("[\033[0;31m-\033[0m] Error in connecting to the server...")
				sys.exit(1)

			signal.signal(signal.SIGINT, self.ctrlC)

			self.download()

		else:
			print("Usage: client.py SERVER_IP_ADDRESS FILENAME")

	def download(self):

		print("[\033[0;32m+\033[0m] Downloading the file...")

		try:

			self.theFile = open("./" + str(sys.argv[2]), 'wb')

		except:

			print("[\033[0;31m-\033[0m] Error in writing the file...")

		p = self.sock.recv(4096)

		while p:
			self.theFile.write(p)
			p = self.sock.recv(4096)

		self.theFile.close()
		self.sock.close()

		print("[\033[0;32m+\033[0m] Download completed!")

		sys.exit(0)

	def ctrlC(self, sig, frame):

		ans = input("Do you want to cancel the downloading file? [y,N]> ")

		if str(ans).lower() == 'y':

			# Cancel the downloading

			os.remove("./" + str(sys.argv[2]))

if __name__ == '__main__':
	netget_client = NetgetClient()
