from collections import Counter
s =raw_input("Enter the string from user \n")
t = Counter(s.split()).most_common()
t = sorted(t)
for i in t:
    print(i)
