# Basic Operations in Python
# baseline course

# Arithmetic Operations
a = 15
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)


# Comparison Operations
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal:", a >= b)
print("Less Than or Equal:", a <= b)


# Logical Operations
x = True
y = False
print("Logical AND:", x and y)
print("Logical OR:", x or y)
print("Logical NOT:", not x)


# Bitwise Operations
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)


# Membership Operations
lst = [1, 2, 3, 4]
print("3 in list:", 3 in lst)
print("5 not in list:", 5 not in lst)


# Identity Operations
c = a
print("a is c:", a is c)
print("a is not b:", a is not b)


# String Operations
s1 = "Jayraj"
s2 = "Pulate"
print("String Concatenation:", s1 + " " + s2)
print("String Repetition:", s1 * 3)
print("String Slicing:", s1[1:4])
print("String Length:", len(s1))
print("String Contains:", "H" in s1)


# List Operations
list1 = [1, 2, 3]
list2 = [4, 5]
print("List Concatenation:", list1 + list2)
print("List Repetition:", list1 * 2)
print("List Slicing:", list1[1:])
list1.append(4)
print("List Append:", list1)
list1.pop()
print("List Pop:", list1)


# Dictionary Operations
d = {"a": 1, "b": 2}
print("Dictionary Keys:", d.keys())
print("Dictionary Values:", d.values())
print("Get Value for Key 'a':", d.get("a"))
d["c"] = 3
print("Add Key-Value Pair:", d)


# Tuple Operations
t = (1, 2, 3)
print("Tuple Access:", t[1])
print("Tuple Length:", len(t))


# Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Set Union:", set1 | set2)
print("Set Intersection:", set1 & set2)
print("Set Difference:", set1 - set2)
print("Set Symmetric Difference:", set1 ^ set2)


# File Operations
with open("example.txt", "w") as f:
    f.write("Hello")
with open("example.txt", "r") as f:
    print("File Read:", f.read())

# Exception Handling
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("Error:", e)

# Function Definition and Lambda Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Jayraj"))

square = lambda x: x ** 2
print("Square of 5:", square(5))

# Class and Object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

person = Person("Jayraj", 22)
print(person.introduce())


# Importing Modules
import math
print("Square Root of 16:", math.sqrt(16))


# Square 
squares = []
for x in range(11):
    squares.append(x**2)
print(squares)
print()

price = 51
txt = f"The price is {price} Rupess"
print(txt)

price = 50
txt = f"The price is {price:.2f} Rupess"
print(txt)


price = 51
str1 = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(str1)


# For Loop
for j in range(5):
    print(j, end=" ")
print()
for i in range(0,21,2):
    print(i)
print() 

# While Loop
count = 0
while(count<= 40):
    print(count, end=" ")
    count +=1

print()

count = 1 
while True:
    print(count, end=" ")
    count = count + 1
    if(count>= 11):
        print(count,end=" ")
        break
    
print()


for y in range(100):
    if y % 2 == 0:
        print(y,end=" ")
        
    else:
        continue

print()

i = 0
while i < 6:
    print(i)
    if i == 3:
        break
    i+=1
    
print()

j = 0
while(j<11):
    j=j+1
    if(j==5):
        continue
    print(j)
