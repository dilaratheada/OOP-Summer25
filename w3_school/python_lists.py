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