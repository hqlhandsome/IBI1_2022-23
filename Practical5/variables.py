#Edinburgh is found at the longitude -3.19. Store this number in a variable called a.
#• Los Angeles is at -118.24. Store this number in a variable called b.
#Haining is found at the longitude 116.39. Store this number in a variable called c.
#• Calculate the longitude distance that Rob travelled to Los Angeles as the difference between a
#and b. Store this value in a variable called d.
#Calculate the longitude distance that Rob travelled to Haining as the difference between and a
#c. Store this value in a variable called e.
a=-3.19
b=-118.24
c=116.39
d=abs(a-b)
e=abs(a-c)
if d < e:
  print ("Haining is further")
elif e < d:
  print ("Los Angeles is further")
else:
  print ("Same")

X=True
Y=False
W=X and Y
Z=X or Y
print (W,Z)
