# create a list
my_list = ["banana", "apple", "kiwi"]

# duplicates are allowed, when printed all list items will be printed
my_list1 = ["banana", "apple", "kiwi", "banana", "kiwi"]

# list length
print(len(my_list))

# list containing different data types
dif_types = ["hello", 40, True, "hi", False]

# type
print(type(dif_types))

# also another way to creat a list
list1 = list(("apple", "banana", "kiwi"))

# print apple from my_list in 2 ways
my_list = ["banana", "apple", "kiwi"]
print(my_list[1])
print(my_list[-3])

# print 3-4-5th items on this_list
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:5])
print(this_list[-5:-3])

# check if an item in in the list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# change an item on the list
thislist1 = ["apple", "banana", "cherry"]
thislist1[1] = "blackcurrant"
print(thislist1)

# when one item is replaced with more than itself 
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) # apple, blackcurrent, watermelon, cherry

# when two items are replaced by one
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) # apple, watermelon

# how to insert an item
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) # apple, watermelon, banana, cherry

# appending an item will put it to the end
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # apple, banana, cherry, orange

# how to extend (combine) lists
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# the extencion doen't have to be a list
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# when removing only the first item is removed not both of them
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# another way to remove a specific index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# another way to remove a specific index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# delete an entire list
thislist = ["apple", "banana", "cherry"]
del thislist

# clear a list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# print all items one by one
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# print all items one by one using their index numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# print all items using while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# print all items using a short hand for loop
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# without list comprehension 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# with list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# only accept items that are not "apple"
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

