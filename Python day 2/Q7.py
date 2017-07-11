i = int(raw_input("Enter matrix size"))
j = int(raw_input("Enter matrix size"))
for k in range (1,i+1):
    if k==1 or k==i:
        print('*'*(j-1) + ' ')
    else:
        print('*' + ' '*(j-2) + '*')
    
