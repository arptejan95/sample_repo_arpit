list = [12,24,35,70,88,120,155]

#enumerate creates a table of values of list with position number i
list = [x for (i,x) in enumerate(list) if i%2!=0]
print(list)
