start_number = int(raw_input("Enter the first value"))
Last_number = int(raw_input("Enter the last value"))
def fib(n):
                  if n < 2:
                      return n
                  return fib(n-1)+ fib(n-2)

for n in range (start_number,Last_number):
    s = fib(n)
    if s < 50:
        print(fib(n))
    else:
        break
