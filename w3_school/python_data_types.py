"""
text type: str
numeric types: int, float, complex
sequence types: list, tuple, range
mapping type: dict
set types: set, frozenset
boolean type: bool
binary types: bytes, bytearray, memoryview
none type: NoneType
"""
x = "Hello World"	#str	
x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	#you cannot convert complex numbers into another type
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType