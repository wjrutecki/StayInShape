# create a program that will ask the users name, age, and reddit username.
# have it tell them the information back, in the format:
#   your name is (blank), you are (blank) years old, and your username is (blank)
# for extra credit, have the program log this information in a file to be accessed later.

name = input("Enter name: ")
age = input("Enter age: ")
username = input("Enter username: ")
output = "Your name is " + name + ", you are " + age + " years old, and your username is " + username + "."

outputFile = open("Challenge1Output.txt", "w")

print(output)
outputFile.write(output)	  

outputFile.write("")
outputFile.close()