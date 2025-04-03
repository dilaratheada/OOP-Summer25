x = 5
y = "Hello World!"
# to leave a comment
"""
use of these are 
also okey to 
leave a comment
"""
x = str(3) # will print '3'
y = int(3) # will print 3
z = float(3) # will print 3.0

a = 'halo'
print(type(a)) # will print <class 'str'>

b = 4
B = 4
# these are NOT the same, python is case sensitive
c = 'hello'
c = "hello"
# these are the same because quotations don't matter

#in my opininon (the correct way) veriables should be named like the following
my_var = 3
MyVar = 2
myvar1 = 2
#you cannot use the following
"""
1myvar = 4
my-var = 2
my var = 9
"""
x, y, z = "orange", "banana", "cherry"
#x = orange, y = banana, z = cherry
x = y = z = 'paper' # x = y = z , printing them seperately will give the same answer - paper
fruits = ['apple', 'banana', 'cherry']
x, y, z = fruits
# x = apple, y = banana, z = cherry
a = 'python'
b = 'is'
c = 'awesome'
print(a, b, c) # puts spaces between veriables
print(a + b + c) # won't put spaces unless there are spaces already put in the variables

x = 5
y = 3
print(x + y) # 8
y = 'python'
print(x + y) # will give an error
print(x, y) # 5 python

x = "awesome"
def myfunc():
    print("Python is" + x)

myfunc() #Python is awesome

def myfunc1():
    x = "fantastic"
    print("Pyhton is" + x) #Pyhton is fantastic

myfunc1()
print("Python is" + x) #Python is awesome

#putting an x veriable won't change the outcome
def myfunc3():
    global x
    x = "perfect"

myfunc3()
# putting an x veriable here will change the outcome (x = "fantastic" will make 'perfect' change to 'fantastic')
print("Python is" + x) #Python is prefect
