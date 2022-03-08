from lib2to3.pgen2.parse import ParseError
import random
import string


class Password:
    def __init__(self, password_length, amount_of_upper_letters, amount_of_special_marks) -> None:
        self.password_length = password_length
        self.amount_of_upper_letters = amount_of_upper_letters
        self.amount_of_special_marks = amount_of_special_marks
        
    def shuffle_string(self, password) -> str:
        pass_list = list(password)
        random.shuffle(pass_list)
        return "".join(pass_list)
    
    def generatepassword(self) -> str:
        length_diff = password_length - (amount_of_special_marks + amount_of_upper_letters)
        special_marks = '!@#$%^&*()_+-=[];,.<>/?'
        choosen_special_marks = "".join([random.choice(special_marks) for i in range(0, amount_of_special_marks)])
        choosen_upper_case_letters = "".join([random.choice(string.ascii_uppercase) for i in range(0, amount_of_upper_letters)])
        choosen_lower_case_letters = "".join([random.choice(string.ascii_lowercase) for i in range(0, length_diff)])
        print(f'{choosen_special_marks} , {choosen_upper_case_letters} , {choosen_lower_case_letters}')
        password = choosen_special_marks + choosen_upper_case_letters + choosen_lower_case_letters
        password = self.shuffle_string(password)
        return password
        

try:  
    password_length = int(input('How long you want your password to be?'))
    amount_of_upper_letters = int(input('How many upper case letters you want to have in password?'))
    amount_of_special_marks = int(input('How many special marks you want to have in your password?'))
    if amount_of_special_marks + amount_of_upper_letters > password_length:
        print('Unable to generated password mispassed arguments!')
    else:
        generated_password = Password(password_length, amount_of_upper_letters, amount_of_special_marks)
        passwd = generated_password.generatepassword()
        print(f'The generated password for you: {passwd}')
    
except ParseError:
    print(ParseError.msg)