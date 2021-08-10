import numpy as np

from SBOX_Calculator import SBOX_Calculator
from Rcon_Calculator import Rcon_Calculator

class Key():

	def __init__(self):
		self.listofKeys = np.ndarray((11,4,4), np.int32)
		self.currentKey = np.ndarray((4,4), np.int32)

	def generateInitialKey(self):
		#self.key = bytearray(secrets.token_bytes(16))
		key = list("Thats my Kung Fu".encode('utf-8'))

		key = np.reshape(key, (4, 4))
		key = np.transpose(key)

		self.currentKey = key
		self.listofKeys[0] = key

	def expand(self, roundnum):

		w3 = self.currentKey[:, 3:4]
		w3 = np.reshape(w3, (4))

		w3 = self.g(w3, roundnum)
		w3 = np.reshape(w3, (4, 1))

		w4 = self.currentKey[:, 0:1]

		w4 = w4 ^ w3
		w5 = w4 ^ self.currentKey[:, 1:2]
		w6 = w5 ^ self.currentKey[:, 2:3]
		w7 = w6 ^ self.currentKey[:, 3:4]

		self.currentKey[:, 0:1] = w4
		self.currentKey[:, 1:2] = w5
		self.currentKey[:, 2:3] = w6
		self.currentKey[:, 3:4] = w7

		self.listofKeys[roundnum+1] = self.currentKey

	def g(self, word, roundnum):

		word = np.roll(word, -1)

		for x, byte in enumerate(word):

			highnibble = (byte >> 4) & 0x0F
			lownibble = byte & 0x0F

			word[x] = SBOX_Calculator.get_val_sbox(highnibble, lownibble)

		rcon = Rcon_Calculator().generateRcon(roundnum)

		for x in range(len(word)):

			if x == 0:
				word[x] = word[x] ^ rcon
			else:
				word[x] = word[x] ^ 0


		return word