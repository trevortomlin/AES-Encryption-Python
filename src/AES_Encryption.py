import secrets
import numpy as np

from Key import Key
from Block_Generator import Block_Generator
from Round_Encryption import Round_Encryption
from Round_Decryption import Round_Decryption
from Transformer import Transformer

class AES_Encryption():

	numOfRounds = 10

	def __init__(self):
		self.key = Key()
		self.key.generateInitialKey()
	
	@staticmethod
	def stateToString(state):

		out = ""

		for col in range(len(state[0])):

			for row in range(len(state)):

				out += str(state[row][col])

				out += " "

		return out


	def encrypt(self, message):

		states = Block_Generator.generate(message)

		encryptedStates = []

		for state in states:		

			state = Transformer.addRoundKey(state, self.key.currentKey)

			for r in range(0, self.numOfRounds-1):
				self.key.expand(r)
				state = Round_Encryption.do_encryption_round(state, self.key.currentKey)

			self.key.expand(9)

			state = Round_Encryption.do_encryption_final_round(state, self.key.currentKey)

			encryptedStates.append(state)

		return encryptedStates

	def decrypt(self, states):

		decryptedStates = []

		for state in states:

			currentKey = self.key.listofKeys[-1]

			state = Round_Decryption.do_decryption_first_round(state, currentKey)

			for r in range(self.numOfRounds-1, 0, -1):
				currentKey = self.key.listofKeys[r]
				state = Round_Decryption.do_decryption_round(state, currentKey)

			currentKey = self.key.listofKeys[0]
			state = Transformer.addRoundKey(state, currentKey)

			decryptedStates.append(state)

		return decryptedStates