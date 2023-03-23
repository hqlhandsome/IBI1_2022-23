#we can use the while-loop to calculate the rabbit number and add the limit to make sure the total number <=100
#when the total number is over 100 the loop stops.
a=1 #a means the generation of the rabbit
m=2 #m means the total number of the rabbit in each generation
while m<=100:
  a=a+1
  m=2*m #two rabbit will produce two new rabbits
  print(a,m)#the number of the rabbit in each generation until we have at least 100 rabbits
  #1st generation has 2 rabbits
  #2nd generation has 4 rabbits
  #3rd generation has 8 rabbits
  #4th generation has 16 rabbits
  #5th generation has 32 rabbits
  #6th generation has 64 rabbits
  #7th generation has 128 rabbits
print(a,m)#the first number 7 is the generation, the second number 128 is the total number of the rabbit.
