#imports
import sys 
import random

#vars 
i = 0
x = 1
options = [] 
count = int(sys.argv[len(sys.argv) - 1])
file = open("list-from-results.txt","w+")

#create a new list of the arguments with the file name and count removed
while x < (len(sys.argv) - 1):
	options.append(sys.argv[x])
	x += 1

#pick a random item from the list of arguments and add it to the file
while i < count:
	file.write(random.choice(options) + "\r\n")
	i += 1

#close the file
file.close()