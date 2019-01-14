# Randomly generated password.

Usually in webpages with account management you can ask for a temporal password to recover your account in case you forgot your real password.
This function can help to generate those random paswords.


### Code:

Importing Libraries:

```python
import string
from random import randrange
```

Declaring the function:

```python
# Default values for this function are a lenght of 7 chars for the password and an alphabeth of ASCII letters and numbers.
def password_gen(id_lenght = 7, alphabet = string.ascii_letters + string.digits):

    id_list = []

    # for the default alphabet this function will include an special random character on a random position on the password. 
    special_char_index = -1 
    if alphabet == string.ascii_letters + string.digits:
        lenght_punctiation = len(string.punctuation) 
        range_punct = randrange(lenght_punctiation)
        special_char = string.punctuation[range_punct]
        special_char_index = randrange(id_lenght)


    for i in range(id_lenght):
        index = randrange(len(alphabet))

        # in this part is where the special character gets added to the password (only if the default alphabed is used)
        if i == special_char_index:
            id_list.append(special_char)
        else:
            id_list.append(alphabet[index])

    id = ''.join(id_list)    

    return id
```

### Calls
#### Calling the password_gen() function with default parameters:

Code:

```python
passwrd = password_gen()
print(passwrd)
```

Output:

```shell
Terminal$ python3 universally_unique_id_gen.py 
Sb429#U
```


#### Calling the password_gen() function with specified lenght and a default alphabet parameters:

Code:

```python
lenght = 15
passwrd = password_gen(lenght)
print(passwrd)
```
or with parameter naming:

```python
lenght = 15
passwrd = password_gen(id_lenght = lenght)
print(passwrd)
```

Output:

```shell
Terminal$ python3 universally_unique_id_gen.py 
0SsX~xYFSIVHo7Z
```


#### Calling the password_gen() function with specified lenght and a default alphabet parameters:

Code:
```python
alpha = 'xyz-654'
passwrd = password_gen(alphabet = alpha)
print(passwrd)
```

Output:

```shell
Terminal$ python3 universally_unique_id_gen.py
5z545zy
```
#### Calling the password_gen() function with specified lenght and a default alphabet parameters:

Code:
```python
lenght = 40
alpha = 'abxy01'
passwrd = password_gen(lenght,alpha)
print(passwrd)
```

or with parameter naming:

```python
lenght = 40
alpha = 'abxy01'
passwrd = password_gen(alphabet = alpha, id_lenght = lenght)
print(passwrd)
```

Output:

```shell
Terminal$ python3 universally_unique_id_gen.py 
0000xbaaxxyx00yya0xa1x1yxabyy0aaxb100x1b
```



