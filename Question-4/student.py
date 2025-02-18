# A university has a Person class with a method introduce() that prints "I am a person."
# A subclass Student overrides this method to print "I am a student." Write the Python
# code demonstrating this behavior.

class Person():
    def introduce(self):
        print("I am a person")

class Student(Person):
    def introduce(self):
        print("I am a student")
