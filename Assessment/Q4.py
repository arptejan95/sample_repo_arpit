n = int(input("Enter a number "))
sum = 0
while (n > 0):
    reminder = n%10
    sum = sum + reminder
    n = n // 10
print("The sum of the digits is %d"%sum)
