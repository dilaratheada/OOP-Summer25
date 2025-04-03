print("It's alright") 
print("He is called 'Johnny'") # if outer quotations are " the inside ones need to be '
print('He is called "Johnny"') # if outer quotations are ' the inside ones need to be "

# a multiline string can be printed out exectly like its written when put inside """these""" or '''these'''
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(a[1]) # will print 'e' because 'H' is 0 not 1

for x in "dilara":
  print(x)
'''
d
i
l
a
r
a
'''
a = "What's up!"
print(len(a)) #count every character and space so the result will be 10

# to check if a certain phrase or character is present in a string
txt = "The best things in life are free!"
print("free" in txt) #True
# we can also check it by putting an if statement
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.") #Yes, 'free' is present.

# to check if a certain phrase or character is NOT present in a string
txt = "The best things in life are free!"
print("expensive" not in txt) #True
# also can check with an if statement
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.") #No, 'expensive' is NOT present.

b = "Hello, World!"
print(b[2:5]) #without including 2nd and 5th terms (llo)

b = "Hello, World!"
print(b[:5]) #Hello

b = "Hello, World!"
print(b[2:]) #llo, World!

b = "Hello, World!" #while counting backword we start from 1 not 0
print(b[-5:-2]) #this will not include 'd' but will include 'o' (orl)

a = "my mind is gone!"
print(a.upper()) #MY MIND IS GONE!

a = "WHERE ARE YOU??"
print(a.lower()) #where are you??

a = " What's on your mind? "
print(a.strip()) #What's on your mind?, without the space infront or end

a = "Hello!"
print(a.replace("H", "J")) #Jello!

a = "Hello, World!"
b = a.split(",")
print(b) #['Hello', ' World!']

a = "Hello"
b = "World"
c = a + b
print(c) #HelloWorld

a = "Hello"
b = "World"
c = a + " " + b
print(c) #Hello World

age = 36
txt = f"My name is John, I am {age}" #this will let us combine a str with int (f-strings)
print(txt) #My name is John, I am 36

price = 59
txt = f"The price is {price} dollars"
print(txt) #The price is 59 dollars

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt) #The price is 59.00 dollars

txt = f"The price is {5 * 6} dollars"
print(txt) #The price is 30 dollars`

#escape character allows you to use double quotes when you normally would not be allowed
txt = "We are the so-called \"Vikings\" from the north." 
#\'	= Single Quote	(allows you to use the same quotation)
txt = 'It\'s alright.'
print(txt) #It's alright.
#\\	= Backslash	(\)
txt = "This will insert one \\ (backslash)."
print(txt) #This will insert one \ (backslash).
#\n	= New Line	
txt = "Hello\nWorld!"
print(txt)
'''
Hello
World!
'''
#\r	= Carriage Return	(same as new line)
txt = "Hello\rWorld!"
print(txt) 
'''
Hello
World!
'''
#\t	= Tab	
txt = "Hello\tWorld!"
print(txt) #Hello   World!
#\b	= Backspace	(erases one character)
txt = "Hello \bWorld!"
print(txt) #HelloWorld!
#\f	= Form Feed	
#\ooo  = Octal value	(a backslash followed by three integers will result in a octal value)
txt = "\110\145\154\154\157"
print(txt) #Hello
#\xhh  = Hex value (a backslash followed by an 'x' and a hex number represents a hex value)
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) #Hello

'''
capitalize() = Converts the first character to upper case
casefold() = Converts string into lower case
center() = Returns a centered string
count() = Returns the number of times a specified value occurs in a string
encode() = Returns an encoded version of the string
expandtabs() = Sets the tab size of the string
find() = Searches the string for a specified value and returns the position of where it was found
format() = Formats specified values in a string
format_map() = Formats specified values in a string
index() = Searches the string for a specified value and returns the position of where it was found
isalnum() = Returns True if all characters in the string are alphanumeric
isalpha() = Returns True if all characters in the string are in the alphabet
isascii() = Returns True if all characters in the string are ascii characters
isdecimal() = Returns True if all characters in the string are decimals
isdigit() = Returns True if all characters in the string are digits
isidentifier() = Returns True if the string is an identifier
islower() = Returns True if all characters in the string are lower case
isnumeric() = Returns True if all characters in the string are numeric
isprintable() = Returns True if all characters in the string are printable
isspace() = Returns True if all characters in the string are whitespaces
istitle() = Returns True if the string follows the rules of a title
isupper() = Returns True if all characters in the string are upper case
join() = Joins the elements of an iterable to the end of the string
ljust() = Returns a left justified version of the string
lstrip() = Returns a left trim version of the string
maketrans() = Returns a translation table to be used in translations
partition() = Returns a tuple where the string is parted into three parts
rfind() = Searches the string for a specified value and returns the last position of where it was found
rindex() = Searches the string for a specified value and returns the last position of where it was found
rjust() = Returns a right justified version of the string
rpartition() = Returns a tuple where the string is parted into three parts
rsplit() = Splits the string at the specified separator, and returns a list
rstrip() = Returns a right trim version of the string
splitlines() = Splits the string at line breaks and returns a list
swapcase() = Swaps cases, lower case becomes upper case and vice versa
title() = Converts the first character of each word to upper case
translate() = Returns a translated string
zfill() = Fills the string with a specified number of 0 values at the beginning
'''