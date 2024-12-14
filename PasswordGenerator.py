import random
import string
def generate_password(letters_count, digits_count, symbols_count):
    letters = string.ascii_letters 
    digits = string.digits          
    symbols =  ['!', '@', '#','$','&']  
    password_letters = ''.join(random.choice(letters) for _ in range(letters_count))
    password_digits = ''.join(random.choice(digits) for _ in range(digits_count))
    password_symbols = ''.join(random.choice(symbols) for _ in range(symbols_count))
    password = password_letters + password_digits + password_symbols
    password = ''.join(random.sample(password, len(password)))
    return password
print(f"Welcome to Password Generator")
letters_count = int(input("Enter the number of letters in the password: "))
digits_count = int(input("Enter the number of digits in the password: "))
symbols_count = int(input("Enter the number of symbols in the password: "))
password = generate_password(letters_count, digits_count, symbols_count)
print(f"Generated Password: {password}")
