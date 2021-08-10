from Transformer import Transformer

class Rcon_Calculator():

	@staticmethod
	def generateRcon(i):

		rcon = 1

		if (i == 0):
			return rcon

		else:

			for r in range(i):
				rcon = Transformer.mul2(rcon)
			
			return rcon