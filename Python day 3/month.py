month = ['january',
        'february',
        'march',
        'april',
        'may',
        'june',
        'july',
        'august',
        'september'
        'october',
        'november',
        'december']
m = raw_input("Enter the month ")
print("Number of the month is " + str(month.index(m.lower())+1))
