# What does this piece of code do?
# Answer: This code first select a random number from 1 to 100, then it will choose another one from 1 to 100 
# and compare the two random numbers. Then it will run the while-loop,it will choose 10 times in total and 
# print the biggest one of the 10 random numbers

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
stored_random_number=0
while progress<10:
	progress+=1
	n = randint(1,100)
	if n > stored_random_number:
		stored_random_number = n

print(stored_random_number)
