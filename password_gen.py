
import string
from random import randrange


def password_gen(id_lenght = 7, alphabet = string.ascii_letters + string.digits):

    id_list = []

    special_char_index = -1 
    if alphabet == string.ascii_letters + string.digits:

        lenght_punctiation = len(string.punctuation) 
        range_punct = randrange(lenght_punctiation)
        special_char = string.punctuation[range_punct]
        special_char_index = randrange(id_lenght)

    for i in range(id_lenght):
        index = randrange(len(alphabet))

        if i == special_char_index:
            id_list.append(special_char)
        else:
            id_list.append(alphabet[index])

    id = ''.join(id_list)    

    return id


print('-------------')
passwrd = password_gen()
print(f'->> Password with default function: {passwrd}')

print('-------------')
lenght = 15
passwrd = password_gen(lenght)
print(f'->> Password with function with lenght of {lenght}: {passwrd}')

print('-------------')
alpha = 'xyz-654'
passwrd = password_gen(alphabet = alpha)
print(f'->> Password with function with an Alphabet = "{alpha}": {passwrd}')

print('-------------')
lenght = 40
alpha = 'abxy01'
passwrd = password_gen(lenght,alpha)
print(f'->> Password with function with lenght of {lenght} and an Alphabet = "{alpha}": {passwrd}')
