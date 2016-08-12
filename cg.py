#!/usr/bin/env

class CryptoGod(object):
	
	def __init__(self, txt):
		self.txt = txt
	def cesr(self,s):
		cry = []
		alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
		for i in self.txt:
			if i in alpha:
				cry.append(alpha[alpha.index(i)+s])
		return  ''.join(cry)

text = raw_input("Please enter what you wish to encryt: ")
to_be = CryptoGod(text)
s = int(raw_input("How many places would you like to shift your text by? "))
print to_be.cesr(s)
