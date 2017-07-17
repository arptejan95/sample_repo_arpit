class strn():

   def __init__(self):
       self.str1 = ''
   
   def enter(self):
       self.str1=raw_input("Enter string: ")

   def prn(self):
       print(self.str1)


strg = strn()
strg.enter()
strg.prn()
