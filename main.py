class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def intro(self):
        return f"My name is {self.name} and i am {self.age} years old."
 
me = Person("Ada Dilara", 19)
print(me.intro())