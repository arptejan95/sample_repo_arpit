n1 =  int(raw_input("Enter the number"))
def power_of_two(n):
       return n > 0 and (n & (n - 1)) == 0
print(power_of_two(n1))
        

