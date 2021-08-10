from AES_Encryption import AES_Encryption

def main():
	
	text = "Two One Nine Two"

	ae = AES_Encryption()

	ct = ae.encrypt(text)
	print(AES_Encryption.stateToString(ct[0]))
	t = ae.decrypt(ct)
	print(AES_Encryption.stateToString(t[0]))

if __name__ == '__main__':
	main()

