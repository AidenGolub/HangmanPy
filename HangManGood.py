#Hangman by Aiden Golub
import sys
import math
import time
import getpass
import random
import urllib.request
print("Welcome to Hangman by Aiden Golub!")
rep = True
while rep == True:
	HANGMAN = (
			"""
			-----
			|   |
			|
			|
			|
			|
			|
			|
			|
			--------
			""",
			"""
			-----
			|   |
			|   0
			|
			|
			|
			|
			|
			|
			--------
			""",
			"""
			-----
			|   |
			|   0
			|  -+-
			|
			|
			|
			|
			|
			--------
			""",
			"""
			-----
			|   |
			|   0
			| /-+-
			|
			|
			|
			|
			|
			--------
			""",
			"""
			-----
			|   |
			|   0
			| /-+-\ 
			|
			|
			|
			|
			|
			--------
			""",
			"""
			-----
			|   |
			|   0
			| /-+-\ 
			|   | 
			|
			|
			|
			|
			--------
			""",
			"""
			-----
			|   |
			|   0
			| /-+-\ 
			|   | 
			|   | 
			|
			|
			|
			--------
			""",
			"""
			-----
			|   |
			|   0
			| /-+-\ 
			|   | 
			|   | 
			|  |
			|
			|
			--------
			""",
			"""
			-----
			|   |
			|   0
			| /-+-\ 
			|   | 
			|   | 
			|  | 
			|  | 
			|
			--------
			""",
			"""
			-----
			|   |
			|   0
			| /-+-\ 
			|   | 
			|   | 
			|  | | 
			|  | 
			|
			--------
			""",
			"""
			-----
			|   |
			|   0
			| /-+-\ 
			|   | 
			|   | 
			|  | | 
			|  | | 
			|
			--------

			"""
			)
	HANGMANEND = (
			"""
			-----
			|   |
			|   0 .
			|	. 	.
			| \-+-/
			|   | .  .
			|   | 
			|  | |    .
			|  | |      .
			|          .  . ..
			--------  .  . . ... ..    
			"""
	)
	def spaceing():
		for x in range(0,35):
			print()
	def line():
		print("________________________________________________________________________________________________________________________")
	print()
	y = 0
	p2=[]
	p2s=[]
	gs=[]
	alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
				"m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
				"y", "z", "hint"]
	while y == 0:
		hangmanMachine = input("(1) or (2) players?: ").lower()
		if hangmanMachine == "1" or hangmanMachine == "2":
			y = 1
	if hangmanMachine == "1":
		Gn=""
		print()
		difL=["1","2","3"]
		e = 0
		while e == 0:
			dif=input("Easy(1) Medium(2) or Hard(3): ").lower()
			if dif not in difL:
				print()
				print("Warning: Please enter a number for the difficulty!")
				print()
			else:
				e = 1
		print()
		print("The secret word is being selected")
		time.sleep(.5)
		t = True
		while t == True:
			word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
			response = urllib.request.urlopen(word_site)
			txt = response.read().decode()
			WORDS = txt.splitlines()
			word = random.choice(WORDS).lower()
			if dif == "1":
				if len(word) < 5:
					t = False
			if dif == "2":
				if len(word) < 8 and len(word) > 4:
					t = False
			if dif == "3":
				if len(word) > 10:
					t = False
		time.sleep(1)
		for i in word:
			p2.append(i.lower())
			p2s.append("_")
		print()
		question = input("The secret word has been chosen. Press (enter) to continue.")
		print()
	if hangmanMachine == "2":
		print()
		Cn=input("Chooser Name: ")
		Gn=input("Guesser Name: ")
		print()
		u = True
		while u == True:
			p = getpass.getpass(prompt=Cn+" starts, please enter the secret word here: ", stream=None)
			if p == "":
				u = True
			else:
				u = False
		word=p
		time.sleep(.25)
		print()
		print("converting word...")
		print()
		for i in p:
			if i == " ":
				p2.append(" ")
				p2s.append(" ")
			else:
				p2.append(i.lower())
				p2s.append("_")
		time.sleep(1)
		question = input(Cn+"'s word has successfuly been imported. Press (enter) to start the game.")
		print()
	line()
	for x in range(0,3):
		print()
	gno = 0
	m = 0
	q = 0
	tx = 0
	z = 0
	used="Letters used:"
	while gno != 110:
		for x in range(0,12):
			print()
		if gno >= 11:
			line()
			if hangmanMachine == "1":
				print("You lost!")
			else:
				print(Gn+" lost!")
			print()
			print(HANGMANEND)
			print()
			print("The word was: "+word)
			line()
			print()
			question = input("Do you want to play again? Y or N: ").lower()
			if question == "n":
				sys.exit()
			else:
				spaceing()
				break
				rep = True
			gno+=1
		if gno < 11:
			x=HANGMAN
			print(x[gno])
			p2ss = str(p2s)[1:-1]
			p2ss = p2ss.replace(',',' ')
			p2ss = p2ss.replace("'",'')
			print("        Word: "+p2ss)
			print()
			print("        Number of guesses left: "+str(11-int(gno))+"/11")
			print()
			print()
			if q > 0:
				print(used)
				print()
			p = 0
			while p == 0:	
				if tx == 0:
					f = " or use a (hint)"
				else:
					f = ""
				if hangmanMachine == "1":
					letGuess = input("Please guess a letter"+f+": ").lower()
				else:
					letGuess = input(Gn+", please guess a letter"+f+": ").lower()
				if letGuess == "hint" and tx == 0:
					r = True
					while r == True:
						letterH = random.choice(p2).lower()
						if letterH == " ":
							r = True
						else:
							r = False
						gs.append(letterH.lower())
						used+=" "+letterH.lower()+" "
					fx = "One letter in the word is: "+letterH
					tx += 1
					z += 1
					gno += 1
					n = 0
					t = 0
					for i in p2:
						if i == letterH:
							del p2s[n]
							p2s.insert(n, i)
							del p2[n]
							p2.insert(n, " ")
							t+=1
						n+=1
				if letGuess == "hint" and tx > 0:
					print()
					print("You have already used your hint!")
				if letGuess == "" or letGuess not in alphabet:
					print()
					print("Please guess a letter!")
					print()
					print()
				elif letGuess in gs:
					print()
					if letGuess != "hint":
						print("You have already guessed that letter!")
					print()
					print()
				else:
					gs.append(letGuess)
					p = 1
			n = 0
			t = 0
			for i in p2:
				if i == letGuess:
					del p2s[n]
					p2s.insert(n, i)
					del p2[n]
					p2.insert(n, " ")
					t+=1
				n+=1
			if letGuess != "hint":
				used+=" "+letGuess+" "
			if t == 0:
				gno+=1
			if "_" not in p2s:
				m+=1
			q+=1
		if m > 0:
			for x in range(0,12):
				print()
			print(HANGMAN[gno])
			p2ss = str(p2s)[1:-1]
			p2ss = p2ss.replace(',',' ')
			p2ss = p2ss.replace("'",'')
			print("        Word: "+p2ss)
			print()
			line()
			if hangmanMachine == "1":
				print("You are the winner!")
			else:	
				print(Gn+", you are the winner!")
			print("The word was: "+word)
			line()
			print()
			question = input("Do you want to play again? Y or N: ").lower()
			if question == "n":
				sys.exit()
			else:
				spaceing()
				break
				rep = True
