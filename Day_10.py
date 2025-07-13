#1.Creating String

single_quote_stings = 'hello'
double_quote_strings = "hello"
triple_quote_strings = '''hello'''


print(single_quote_stings)


print(double_quote_strings)


print(triple_quote_strings)

multiline_string = '''
this is line 1 in my story 
this is line 2 in my story
this is line 3 in my story
'''
print(multiline_string)

#2.Accessing Char

single_quote_stings [1]


#3.Slicing a String

single_quote_stings[:4]

multiline_string[:10]

double_quote_strings[-1]

#5.String Concatenation

"Hello"+" "+"Rushi"+"!"

#6.String Repetition

"ha "*3 + "!"

#7.String Length

x = "Hello"
 

len(x)

#8.Checking Substring

# substring - string which is a part of the main string
# "Hello World" --> "World"

x = "Hello World "
print ("" in x)

#9. String Method / Function


name = "Rushi"

name.lower()

# join , strip, replace


# 10. String Formatting - F String

name = "Rushi"
print(f"My name is {name}!")
