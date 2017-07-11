i = int(raw_input("Enter matrix sixe"))
j = int(raw_input("Enter matrix size"))
for k in range (1,i+1):
    if k==1:
        print(' ' + '*'*(j-2) + ' ')
    elif k%2==0 and k==i/2:
        print ('*'*j )
    elif k%2!=0 and k==(i+1)/2:
        print('*'*j)
    else:
        print('*' + ' '*(j-2) + '*')
    
