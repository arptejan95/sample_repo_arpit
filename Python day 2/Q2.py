T = raw_input("Choose C or F")
i = int(raw_input("Enter the value of temperature"))
if T=="C":
    print("The temperature in fahrenheit is %dF"%((i*9/5)+32))
elif T=="F":
    print("The temperature is %dC"%((i-32)*5/9))
 
