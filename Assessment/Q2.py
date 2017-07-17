lam=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
rows=int(raw_input("Enter the no. of rows to print"))
m=0
for i in range(rows):
   for j in range(i+1):
       if j==i:
           print str(lam[m])
           m=m+1
       else:
           print str(lam[m]),
           m=m+1
