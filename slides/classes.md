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