#Reversing a string using function

""""
Define a function called reverse_string that accepts one argument (a string).
Return the reversed version of the string.
Try using string slicing as a first approach.
"""

def reversed_string():
    user_input = input("Enter your string: ").strip()
    result= user_input[::-1]
    print(f"Reversed String: {result}")
reversed_string ()
