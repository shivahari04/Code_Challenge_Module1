# Reverse a string using simple for loop

"""
Writing a second version using a for loop to build the reversed string manually.
"""

user_input= input("Input your string: ")
reversed_string=""
for letter in user_input:
    reversed_string=letter+reversed_string
print(f"Reversed String: {reversed_string}")

