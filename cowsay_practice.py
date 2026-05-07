import cowsay as cs

name = input("Enter your name: ")
cs.cow(f'Hello, {name}! Welcome to the world of Python programming!')


# Understanding f-strings
# Notice the f before the string: f"Hello {name}!". This is called an f-string (formatted string). It allows you to insert variables directly inside a string using curly braces {}.

# age = 25
# print(f"I am {age} years old")   # Output: I am 25 years old

