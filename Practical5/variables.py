#a is the longitude of Edinburgh
#b is the longitude of Los Angeles
#c is the longitude of Haining
#d is the longitude distance that Rob travelled to Los Angeles, as the difference between a and b
#e is the longitude distance that Rob travelled to Haining, as the difference between a and c
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
#Rob travel further to Haining than Los Angeles

X=True
Y=False
W=X and Y
Z=X or Y
print (W,Z)
# W means false and Z means true

