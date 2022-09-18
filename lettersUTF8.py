# Given a string which contain letters(uppercase and lowercase), numbers, and specialcharacters,
# return the same string in all lowercase.For example, if the function receives: “Ñañito, QUÉ bien!
# THIS is a sample text, Lorem Ipsum, 2 Be Converted.”The function should return: “ñañito, qué bien! 
# this is a sample text, lorem ipsum, 2 be converted.”The function should consider converting: 
# All characters from A-Z, Á, É, Í, Ó, Ú and Ñ. Othercharacters will remain the same.
# Limitation:The conversion should be done considering the ASCII values. 
# bviously you CAN’T use thefunctions provided by the language (toLowercase(), lowercase(), etc.). 
# You CAN’T have ahuge switch statement with cases for each letter, or lots of if/else statements.
# This function will receive an string and return an string

vowels =['a','e','i','o','u']
vowels2 = ['á', 'é', 'í', 'ó', 'ú','ñ']
vowels3 = ['A', 'E', 'I', 'O', 'U','Ñ']


# chr(97)
letters = list(map(lambda x: ord(x), vowels3))
print (letters)