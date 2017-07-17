import re
emailAddress = input("Enter the string")

#to match words - \w
part2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(pat2,emailAddress)
print (r2.group(1))
