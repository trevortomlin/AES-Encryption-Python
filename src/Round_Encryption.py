from Transformer import Transformer

class Round_Encryption():

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