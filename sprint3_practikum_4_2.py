# Напишите декоратор obfuscator
def obfuscator(func):
    def wrapper():
        dictionary = func()
        name = dictionary['name']
        passwd = dictionary['password']
        dictionary['name'] = f'{name[0]}{"*"*(len(name)-2)}{name[-1]}'
        dictionary['password'] = '*' * len(passwd)
        print(dictionary)
        return dictionary
    return wrapper

@obfuscator
def get_credentials():
    return {
        'name': 'StasBasov',
        'password': 'iamthebest'
    }


print(get_credentials())