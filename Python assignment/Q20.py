class Person(object):
    def getGender(self):
        return "Unknown"

#define male class
class Male(Person):
    def getGender(self):
        return "Male"

#define female class
class Female(Person):
    def getGender(self):
        return "Female"

Male = Male()
Female= Female()
print(Male.getGender())
print(Female.getGender())
