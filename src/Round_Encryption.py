from Transformer import Transformer

class Round_Encryption():
	"""
	Description:

		Performs the transformation that make up the encryption round on a state.

	Functions:

		do_encryption_round -> state
		do_encryption_final_round -> state

	"""

	@staticmethod
	def do_encryption_round(state, key):

		state = Transformer.subBytes(state)
		state = Transformer.shiftRows(state)	
		state = Transformer.mixColumns(state)
		state = Transformer.addRoundKey(state, key)

		return state	

	@staticmethod
	def do_encryption_final_round(state, key):

		state = Transformer.subBytes(state)
		state = Transformer.shiftRows(state)
		state = Transformer.addRoundKey(state, key)

		return state	