# Classes are declared this way
class ClassyTwo:

    label: str

    # Python uses  __init__ for constructor all class methods accept self as argument
    def __init__(self, label):
        self.label = label

    def __str__(self):
        return self.label


if __name__ == '__main__':
    raise Exception("This should not run")
    
