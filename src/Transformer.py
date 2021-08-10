import numpy as np

from SBOX_Calculator import SBOX_Calculator

class Transformer():

	@staticmethod
	def subBytes(state):

		for col in range(len(state)):

			for row in range(len(state)):

				byte = state[row][col]

				highnibble = (byte >> 4) & 0x0F
				lownibble = byte & 0x0F

				state[row][col] = SBOX_Calculator.get_val_sbox(highnibble, lownibble)

		return state	

	@staticmethod
	def invSubBytes(state):

			for col in range(len(state)):

				for row in range(len(state)):

					byte = state[row][col]

					highnibble = (byte >> 4) & 0x0F
					lownibble = byte & 0x0F

					state[row][col] = SBOX_Calculator.get_val_invsbox(highnibble, lownibble)

			return state

	@staticmethod
	def shiftRows(state):

		for x in range(len(state)):

			state[x] = np.roll(state[x], -x)

		return state

	@staticmethod
	def invShiftRows(state):

		for x in range(len(state)):

			state[x] = np.roll(state[x], x)

		return state

	@staticmethod
	def mixColumns(state):
		
		for x in range(len(state)):

			col = state[:, x:x+1]

			colcopy = col.copy()

			colcopy[0] = Transformer.mul2(col[0]) ^ Transformer.mul3(col[1]) ^ col[2] ^ col[3]
			colcopy[1] = col[0] ^ Transformer.mul2(col[1]) ^ Transformer.mul3(col[2]) ^ col[3]
			colcopy[2] = col[0] ^ col[1] ^ Transformer.mul2(col[2]) ^ Transformer.mul3(col[3])
			colcopy[3] = Transformer.mul3(col[0]) ^ col[1] ^col[2] ^  Transformer.mul2(col[3])

			state[:, x:x+1] = colcopy.copy()

		return state
	
	@staticmethod	
	def invMixColumns(state):
		state = Transformer.mixColumns(state)
		state = Transformer.mixColumns(state)
		state = Transformer.mixColumns(state)

		return state

	@staticmethod
	def addRoundKey(state, key):
		
		state = state ^ key

		return state

	@staticmethod
	def mul2(v):

		# Multiply by 2
		s = v << 1

		s &= 0xff

		# Check if high bit before shift was 1
		# and xor with x^8 + x^4 + x^3 + x + 1 to make the result 8 bits in length
		if (v & 128) != 0:
			s = s ^ 0x1b

		return s

	@staticmethod
	def mul3(v):
		return Transformer.mul2(v) ^ v