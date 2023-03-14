#n means the number of the hexagon, h means the number of the dots. We can use While-loop to calculate the the hexagon 
#sequence and computes and displays the first five values of the hexagon sequence
n=1
while n<=5:
  h=2*n*(2*n-1)*0.5
  n=n+1
  print(h)
#h1=1.0 h2=6.0 h3=15.0 h4=28.0 h5=45.0
