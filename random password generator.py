import random
import string

string_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string_num = '0123456789'
string_special = '~!@#$%^&*()'

def userInput():
    length = int(input("Enter the length of the password: "))
    use_special_chars = input("Include special characters?(yes/no): ").lower() == 'yes'
    use_numbers = input("Include numbers?(yes/no): ").lower() == 'yes'
    complexity_level = input("Enter complexity level (low, medium, high): ").lower()
    return length, use_special_chars, use_numbers, complexity_level

def generate_password(length, use_special_chars, use_numbers, complexity_level):
    password = ''
    char_set = string_char
    
    if complexity_level == 'medium':
        char_set += string_num
    elif complexity_level == 'high':
        char_set += string_num + string_special
    
    if use_numbers:
        password += random.choice(string_num)
    if use_special_chars:
        password += random.choice(string_special)
    
    for _ in range(length - len(password)):
        password += random.choice(char_set)
    
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

if __name__ == '__main__':
    length, use_special_chars, use_numbers, complexity_level = userInput()
    generated_password = generate_password(length, use_special_chars, use_numbers, complexity_level)
    print("\nGenerated Password:", generated_password)