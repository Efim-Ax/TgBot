# I am single line comment
"I am single line comment too"

""" Multi-line comment used
print("Python Comments") """

# name = input("Enter your name: ")
# print(f"Hello, {name}! You look good!")
# print("Hello, "+name+"! You look good!")

# Prompting the user for input
while True:
    try:
        age_input = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please, enter your age in numbers")

# Converting the input to an integer
age = int(age_input)

# Checking conditions based on user input
if age < 0:
    print("Please enter a valid age.")
elif age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")