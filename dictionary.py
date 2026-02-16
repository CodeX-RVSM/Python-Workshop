# Subject Dictionary
subject = {
    "maths": 90,
    "pythhon": 89,
    "java": 96,
    "c": 56,
    "web": 87
}

# Print dictionary
print(subject)

# Total using sum()
total = sum(subject.values())
print(total)

# Total using loop
total_sum = 0
for key in subject:
    total_sum += subject[key]
print(total_sum)

# Maximum marks
max_marks = max(subject.values())
print(max_marks)

# Minimum marks
min_marks = min(subject.values())
print(min_marks)

# Dictionary update example
x = {"a": 1, "b": 2}
y = {"c": 6, "d": 9}

x.update(y)
print(x)

# Clear dictionary
x.clear()
print(x)

# Print items of y
print(y.items())
