#Caeser_Cipher Encoded
"""
Define a function called caesar_cipher that accepts:
a string text
an integer shift
Return a new string with each alphabetical character shifted by the shift amount.
Keep the case (uppercase/lowercase) the same.
Do not change non-letter characters like punctuation, spaces, or numbers.
a string text
an integer shift
"""

def caesar_cipher(text,shift):
    answer = ""
    
    for char in text:
        if char.isalpha():
            
            #To determine if we start from 'A' or 'a'
            letter = ord('A') if char.isupper() else ord('a')
            shifted_letter = chr((ord(char) - letter + shift) % 26 + letter)
            answer += shifted_letter
        
        else:
            answer +=char
    
    return answer   

print("\nEncoding Caeser_Cipher!\n")
user_input = input("Enter your message: ")
try:
    user_shift = int(input("\n Enter your shift value (default is 3): "))
    encoded_message = caesar_cipher(user_input, user_shift)
    print(f"Encoded message: {encoded_message}")
except ValueError:
    print("Value Error - Please input correct value!!!")
