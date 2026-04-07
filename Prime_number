# Check for Prime number
"""
Define a function called is_prime that takes one integer as input.
Return True if the number is prime and False otherwise.
Use a loop to check divisibility — don’t use any external libraries or built-in prime checkers.
"""
def is_prime(user_number):
    
    if user_number<2:
        return False
    elif user_number ==2:
        return True
    elif user_number %2 ==0 :
        return False
    
    for n in range(3, int(user_number**0.5)+1, 2):
        if user_number %n ==0:
            return False
    return True
    
user_number = int(input("Enter your number: "))
answer = is_prime(user_number)
print(answer)
        
    