def opn(choice,x,y):
   if choice==1:
       ans=x+y
   if choice==2:
       ans=x-y
   if choice==3:
       ans=x*y
   if choice==4:
       ans=x/y
   print ("Answer for the opn is %f"%ans)
   x=int(raw_input("1.Continue  2.Exit"))
   if x==1:
       print ("Answer for the opn in %f"%Check())

def Check():
   import re   #####
   print("Available Choices.")
   print("1.Add.Enter a and b for a+b")
   print("2.Subtract. Enter a and b for a-b")
   print("3.Multiply. Enter a and b for a*b")
   print("4.Divide. Enter a and b for a/b")
   lam=int(raw_input("Enter your operation choice"))
   if lam not in [1,2,3,4]:
       print("Enter the correct Option")
       Check()
   else:
       x=(raw_input("CHOOSE a"))
       print x
       y=(raw_input("CHOOSE b"))
       print y
       if lam==4 and y==0:
           print("Opn is divide and b=0.Choose Again")
           Check()
       
       regex = re.compile(r'(\d+|\s+)')  #####
       A=regex.split(str(x))
       lam1=True
       lam2=True
       for i in A:
           if ((i.isdigit()==True) or (i=="") or (i=="."))==False:
               lam1=False
       B=regex.split(str(y))
       for i in B:
           if ((i.isdigit()==True) or (i=="") or (i=="."))==False:
               lam2=False
       if ((lam1) and (lam2))==False:
           print("Improper Inputs")
           Check()
       return(opn(lam,float(x),float(y)))
       
Check()
