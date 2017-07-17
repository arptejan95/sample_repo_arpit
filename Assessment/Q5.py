a = [int(x) for x in raw_input().split()]
a=sorted(a)
print("First Missing number is: ")
for b in range(0,a[-2]):
   if a[b+1]!=(a[b]+1):
       print(a[b]+1)
       break
