# Classes are declared this way
class Classy:

    label: str

    # Python uses  __init__ for constructor all class methods accept self as argument
    def __init__(self, label):
        self.label = label

    def __str__(self):
        return self.label


# Python uses indentation instead of { } or begin end. 
# Since the following code is not indented, it will execute if the class is run
classy = Classy('Hello, Classes!')
print(classy)