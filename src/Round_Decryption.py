from Transformer import Transformer

class Round_Decryption():

	@staticmethod
	def do_decryption_round(state, key):

		state = Transformer.addRoundKey(state, key)
		state = Transformer.invMixColumns(state)
		state = Transformer.invShiftRows(state)
		state = Transformer.invSubBytes(state)

		return state

	@staticmethod
	def do_decryption_first_round(state, key):

		state = Transformer.addRoundKey(state, key)
		state = Transformer.invShiftRows(state)
		state = Transformer.invSubBytes(state)

		return state