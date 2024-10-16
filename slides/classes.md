# Python classes
``` python
class Classy:

    label: str

    def __init__(self, label):
        self.label = label

    def __str__(self):
        return self.label
```

# Importing and instantiating classes
``` python
classy = Classy('Hello, Classes!')
print(classy)
```

Check out the [example code](../assets/examples/classy.py) of a class

## Side effects
Python executes unindented code in loaded files, avoid by specifying that code should only run if current file is the entry:
``` python
if __name__ == '__main__':
    print("This text only prints if this file is the entry point")
```
And also this [example](../assets/examples/classy.py) of entry point side effects