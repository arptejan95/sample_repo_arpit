class Error(Exception):
   pass

class ValueTooSmallError(Error):
   pass

class ValueTooLargeError(Error):
   pass

number = 10

while True:
   try:
       i = int(input("Enter a number: "))
       if i < number:
           raise ValueTooSmallError
       elif i > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("This value is too small, try again!")
       print()
   except ValueTooLargeError:
       print("This value is too large, try again!")
       
print()
print("Congratulations! You guessed it correctly.")
