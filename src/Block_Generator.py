import numpy as np

class Block_Generator():
	"""
	Description:
		Splits the user's message into blocks of 16 bytes.
	
	Functions:

		generate -> 3d numpy array

	"""

	@staticmethod
	def generate(string):

		#padding if string < block size (16 bytes)
		while (len(string) % 16 != 0):
			string += '0'
		
		states = bytearray(string.encode('utf-8'))

		states = np.reshape(states, (-1, 4, 4))
		states = np.transpose(states, (0, 2, 1))

		return states