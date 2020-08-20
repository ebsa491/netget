# License : GPL v3.0
# Created by Saman Ebrahimnezhad .
#
# RSA Cipher Class
# You can use this script personally but pay attention to the license file.

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Random import new as Random
from base64 import b64encode, b64decode

class RSAClass:
	def __init__(self):
		rng = Random().read

		key = RSA.generate(2048, rng)

        self.__publicKey = key.publickey().exportKey('PEM')
        self.__privateKey = key.exportKey('PEM')

		return True

    def publicKey(self):
        return self.__publicKey

    def privateKey(self):
        return self.__privateKey
