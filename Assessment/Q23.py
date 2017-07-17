filename = 'Q16 text file.txt'

s = raw_input('Enter the string')

with open(filename, 'a') as f:

   f.write(s)