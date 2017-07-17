a = raw_input("Enter the list: ").split(',')
flag = True
for i in range(0,len(a)-2):
   if (int(a[i])+int(a[i+1]))!= int(a[i+2]):
       flag = False
if flag==True:
   print("Additive sequence")
else:
   print("Not an additive sequence")
   
