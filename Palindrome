#Palindrome

"""
Define a function called is_palindrome that accepts a single string.
Return True if the string is a palindrome, and False otherwise.
Normalize the string by:
Converting it to lowercase
Removing spaces (and optionally punctuation)
Reverse the normalized string and compare it to the original normalized version.
Converting it to lowercase
Removing spaces (and optionally punctuation)
"""
def is_palindrome(text):
    text=text.lower().strip()
    reverse_string=text[::-1]
    return text==reverse_string
user_input = input("Enter your text: ")

if is_palindrome(user_input):
        print(True)
        print(f"{user_input} is a palindrome")
else:
        print(False)
        print(f"{user_input} is not a palindrome")
