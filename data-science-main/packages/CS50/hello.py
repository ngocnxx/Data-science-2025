
print ("hello, world")

## Libraries, function get_string 
from cs50 import get_string
answer = get_string("What's your name? ")
# print("hello, " + answer)
print(f"hello, {answer}")

## Function input
answer=input("What's your name?")
print(f"hello, {answer}")

## creating a calculator
from cs50 import get_int

x = get_int("x: ")
y = get_int("y: ")

print(x + y)

## prompt user for input x&y 
x = int(input("x: "))
y = int(input("y: "))
print(x + y)

## compare 2 inputs: x and y 
from cs50 import get_int

x = get_int ("x: ")
y = get_int ("y: ")

if x < y:
    print ("x is less than y")
elif x > y:
    print ("x is greater than y")
else: print ("x is equal to y")

## compare two strings using function input
t = input("t: ")
h = input("h: ")

if t == h:
    print("Same")
else:
    print("Different")

## agree function for terms of conditions
s = input("Do you agree?").lower()
# s = s.lower()

## Array of possible yes answers 
if s in ["y", "yes"]:
    print("Agreed")
elif s in ["n", "no"]:
    print("Not agreed")

## loops
i=0
while i < 3:
    print ("meow")
    i+=1
for i in range(3):
    print("helo, world")

## loop forever
while True:
    print("meow")


## named parameters - end:
before = input ("Before:")
print ("After: ", end=" ")

print(before.upper())

# for c in before:
#     print(c.upper(), end=" ")
# print()

after=before.upper()
print ("After: {after}")

print (f"After: {before.upper()}")