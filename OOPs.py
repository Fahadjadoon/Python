#OOPS Concepts

class Student: #Class name should start with capital alphabet

    #constructor
    def __init__(self, name):
        self.name = name
    
    @staticmethod
    def greetings():
        print("Greetings all new students !!")

    #method
    def online(self):
        print("Names of the students who are taking  online classes", self.name)

#Creating object of the class
s1 = Student('Fahad')
s2 = Student('Umer')

#calling method of the class
Student.greetings()
s1.online()
s2.online()


