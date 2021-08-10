import numpy as np

class Block_Generator():

	@staticmethod
	def generate(string):

		#padding if string < block size (16 bytes)
		while (len(string) % 16 != 0):
			string += '0'
		
		state = bytearray(string.encode('utf-8'))

		state = np.reshape(state, (-1, 4, 4))
		state = np.transpose(state, (0, 2, 1))

		return state