from classy import Classy
from classy_two import ClassyTwo

# Loading the classy python file will execute code outside of any class.
# This can be avoided with 
# if __name__ == '__main__':
# Check out classy_two.py

classy = Classy('Hello, Side effects!')
print(classy)

classy_two = ClassyTwo('Hello, Pure!')
print(classy_two)
