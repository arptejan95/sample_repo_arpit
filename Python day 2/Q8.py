i = int(raw_input("Enter matrix size"))
j = int(raw_input("Enter matrix size"))
for k in range(1,i+1):
    if k==1 or k==i:
        print('*'*j)
    elif i%2==0 and k==i/2:
        print('*'*(j-1))
    elif i%2!=0 and k==(i+1)/2:
        print('*'*(j-1))
    else:
        print('*')
    
