class Person:
    """This is a person class"""
    age = 10

    def greet(self):
        print("Hello")

#create a new object of Person Class
harry = Person()

#Output <function Person.greet>
print(Person.greet)

# Output: <bound method Person.greet of <__main__.Person object>>
print(harry.greet)

#Calling object's greet() method
#Output : Hello
harry.greet()

#Ouput : None
print(harry.greet())