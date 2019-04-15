#!/usr/bin/python
import zipfile
"""
	Zipfile password cracker using a brute-force dictionary attack
"""
def extractFile(zFile, password):
	try: 
		zFile.extractall(pwd=password.encode())
		return(password)
	except: 
		return
		
def main():

	zipfilename = '2018 Tax Information.zip'
	dictionary = '6digits5.txt'

	password = None
	result = None
	zFile = zipfile.ZipFile(zipfilename)
	with open(dictionary, 'r') as f:
		for line in f.readlines():
			password = line.strip('\n')
			guess = extractFile(zFile, password)
			#print(guess)
			if guess != (None): 
				print("Password found: " + password)
			

main()



