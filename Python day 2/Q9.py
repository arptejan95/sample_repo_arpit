i= int(raw_input("Enter matrix size "))
j= int(raw_input("Enter matrix size "))

if i<=4 or j<=4:
   print("Please enter matrix size greater than 4 by 4")
else:
   for k in range(1,i+1):
       if k==1 or k==i:
           print(' '+'*'*(j-2)+' ')
       elif i%2==0 and k==i/2:
           print('*'+' '+'*'*(j-2))
       elif i%2!=0 and k==(i+1)/2:
           print('*'+' '+'*'*(j-2))
       elif k<=i/2:
           print('*')
       else:
           print('*'+' '*(j-2)+'*')
