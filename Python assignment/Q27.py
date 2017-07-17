tp=(1,2,3,4,5,6,7,8,9,10)
li=list()

#creating another tuple with even numbers in first tuple
for i in range(0,len(tp)):
    if tp[i]%2==0:
        li.append(tp[i])

tp2=tuple(li)
print(tp2)
