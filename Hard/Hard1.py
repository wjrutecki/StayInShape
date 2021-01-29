#
# we all know the classic "guessing game" with higher or lower prompts.
# a program that will guess numbers between 1-100,
# and respond appropriately based on whether users say that the number is too high or too low
#

import msvcrt
import os
import random

os.system('cls')

print("\nHello! I'm here to guess your number!\n")
print("Think of a number between 1 and 100 and I'll guess it!")
print("\nIf your number is:")
print("    Higher: press the Up arrow key.")
print("    Lower: press the Down arrow key.")
print("If I'm right, press the enter key!")  
print("\nWhen ready, press enter!")
input("")

lowBound = 0
highBound = 100
guess = random.randint(1,100)
print("Is your number {}?".format(guess))
while True:
	if msvcrt.kbhit():
		keyPress = msvcrt.getch()
		if keyPress == chr(27).encode():
			break
		elif keyPress == chr(13).encode() or keyPress == b'y':
			print("I win!")
			break
		elif keyPress == b'\xe0':
			keyPress = msvcrt.getch()
			if keyPress == b'H':
				lowBound = guess
			elif keyPress == b'P':
				highBound = guess
		if highBound == lowBound + 1:
			print("Uh oh, I failed! Are you sure you didn't change it?")
			print("\nLet's start over!\n")
			lowBound = 0
			highBound = 100
		guess = int((highBound+lowBound)/2)
		print("Is your number {}?".format(guess))
