from AES_Encryption import AES_Encryption

def main():
	
	text = "Two One Nine Two"

	ae = AES_Encryption()
	ae.generateInitialKey()

	ae.generateBlock(text)
	ae.encrypt(text)
	ae.decrypt()

if __name__ == '__main__':
	main()

