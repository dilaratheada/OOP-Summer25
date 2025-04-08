#1 assign multiple values in one line
x, y, z, = "carrot", "banana", "tomato"

#2 create a varibale outsude of the function, then use it inside the function
x = "perfect"
def my_func():
    print("you look" + x)

my_func()

#3 show the 3 numeric types in Python
x = 1   #int
y = 2.7 #float
z = 5j  #complex

#4 print the types of the variables above
print(type(x))
print(type(y))
print(type(z))

#5 try to print "o, Wor" from Hello, World!
s = "Hello, World!"
print(s[4:-3])

#6 print and replace H with J in "Hello, World!"
p = "Hello, World!"
print(p.replace("H", "J"))

#7 create an f-string
age = 19
txt = f"I am {age} years old."
print(txt)

#8 check if a sentence ends with something
x = "Hello, World."
if x.endswith("World!"):
    print("True")
else:
    print("False")

#9 merge two variables into one
a = "Python"
b = "code"
c = a + " " + b
print(c)

#10 print the fruite in the list
my_list = ["juice", "kiwi", "flower", "dance", "club"]
print(my_list[1])