import re
alphabet = raw_input("Enter alphabet")
if (bool(re.search('[aeiou]',alphabet)) or bool(re.search('[AEIOU]',alphabet))):
    print("%s is a vowel"%alphabet)
else:
    print("%s is a consonant"%alphabet)
