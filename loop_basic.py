/*
Python has two main types of loops:

for loops: These are used to iterate over a sequence (like a list, tuple, string, or range) or other iterable objects. They execute a block of code for each item in the sequence.
while loops: These execute a block of code as long as a given condition is true. You need to make sure that the condition eventually becomes false to avoid an infinite loop.
You can also use break and continue statements within loops to control their execution flow. break exits the loop entirely, while continue skips the rest of the current iteration and moves to the next one.


explain the difference between for loop and while loop , with the coding examples
Certainly! I can explain the difference between for and while loops in Python and provide code examples for each.

for loop:

A for loop is used for iterating over a sequence (like a list, tuple, string, or range) or other iterable objects. You typically use a for loop when you know in advance how many times you want to loop or when you want to iterate over the elements of a collection.

Here's a simple example of a for loop using range():

# # Example of a for loop
# print("For loop example:")
# for i in range(5):  # This will loop 5 times, with i taking values from 0 to 4
#   print(i)

while loop:

A while loop, on the other hand, executes a block of code as long as a given condition is true. You use a while loop when you don't know exactly how many times you'll need to loop, and the loop continues until a specific condition is met. It's important to ensure that the condition eventually becomes false to avoid an infinite loop.

Here's a simple example of a while loop:

# Example of a while loop
# print("\nWhile loop example:")
# count = 0
# while count < 5:  # This loop continues as long as count is less than 5
#   print(count)
#   count += 1 # Increment count to eventually make the condition false

*/
