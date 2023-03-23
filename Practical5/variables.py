a=-3.19 #a is the longitude of Edinburgh
b=-118.24 #b is the longitude of Los Angeles
c=116.39 #c is the longitude of Haining
d=abs(a-b) #d is the longitude distance that Rob travelled to Los Angeles, as the difference between a and b
e=abs(a-c) #e is the longitude distance that Rob travelled to Haining, as the difference between a and c
# use if, elif, else to judge which distanse is greater
if d < e:
  print ("Haining is further")
elif e < d:
  print ("Los Angeles is further")
else:
  print ("Same") #Rob travel further to Haining than Los Angeles

X=True
Y=False
W=X and Y
Z=X or Y
print (W,Z) # W means false and Z means true

