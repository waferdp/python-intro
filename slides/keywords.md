# How do i \<do thing\> in Python?
Python is slightly different from C#, Java, and Javascript, for example:

## if statements
``` python
a = 33
b = 200
if b > a:
  print("b is greater than a")
```
scope is defined by indentation, not by { }. The code block above will work, but the block below will raise an error
``` python
a = 33
b = 200
if b > a:
print("b is greater than a")
```

## for loops
``` python
for fruit in ['apple', 'banana', 'cherry']:
    print (fruit)
```

## lambda functions
``` python
fruits = ['apple', 'banana', 'cherry']
x = list(map(lambda f: f.upper(), fruits))

print(x)
```
will print 
['APPLE', 'BANANA', 'CHERRY']

## Check out:
https://www.w3schools.com/python/default.asp

[Previous](/slides/classes.md) \
