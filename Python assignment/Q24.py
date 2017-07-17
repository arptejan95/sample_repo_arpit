import re
s = input("Enter the String")

#finds all substring using regex
print(re.findall("\d+",s))
