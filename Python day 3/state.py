my_dict = {'alwar':'rajasthan', 'surat': 'gujrat', 'chennai':'tamilnadu'}
city = raw_input("Enter the state ")
print my_dict.keys()[my_dict.values().index(city)]
