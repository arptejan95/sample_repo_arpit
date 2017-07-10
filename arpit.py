import sys
a = sys.argv[1]
b = a[::-1]
if a.lower() == b.lower():
    print('It is palindrome')
else:
    print('It is not palindrome')