import random,string
def password_generator(letters_count,digits_count,symbol_count):
    password_str =''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    password_str +=''.join((random.choice(string.digits) for i in range(digits_count)))
    password_str +=''.join((random.choice(string.punctuation) for i in range(symbol_count)))
    
    password_list = list(password_str)
    random.shuffle(password_list)
    final_password = ''.join(password_list)
    return final_password

min_password_length = 6

while True:
    password_length = int(input('Enter your password length: '))
    
    if password_length >= min_password_length:
        print('password generating...')
        break
        
    elif password_length < min_password_length:
        print('password too short,choose a higher number')
        
letters_length = int(input('how many letters would you like in your password?: '))
numbers_length =int(input('how many numbers would you like in your password?: '))
symbol_length = int(input('how many symbol would you like in your password?: '))

password = password_generator(letters_length,numbers_length,symbol_length)
print(password)
