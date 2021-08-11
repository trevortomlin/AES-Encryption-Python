from Transformer import Transformer

class Rcon_Calculator():
	"""
	Description:

		Generate RCON on the fly.

	Functions:

		generateRcon -> int

	"""

	@staticmethod
	def generateRcon(i):

		rcon = 1

		if (i == 0):
			return rcon

		else:

			for r in range(i):
				rcon = Transformer.mul2(rcon)
			
			return rcon