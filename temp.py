def is_include_digit(password):
    for i in range(len(password)):
        if password[i].isdigit():
            return True
    raise ValueError('Пароль должен содержать хотя бы одну цифру')

def is_include_all_register(password):
    for i in range(len(password)):
        if password[i].isupper():
            return True
    return False


def is_include_only_latin(password):
    return password.isascii()


def check_password_dictionary(password):
    with open('easy_passwords.txt') as f:
        if password in f.read():
            return True
    return False

passwd = 'sadadAAAA123123'

print(check_password_dictionary(passwd))
