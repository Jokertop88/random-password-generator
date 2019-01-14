# Randomly generated password.

Usually in webpages with account management you can ask for a temporal password to recover your account in case you forgot your real password.
This function can help to generate those random paswords.

password_gen(object)
 1.  ```password_gen() -> str```
Desc.

 2.  ```password_gen(int) -> str```

 3. ```password_gen(alphabet = String) -> str```

 4. ```password_gen(lenght,alpha)```
Desc.



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

### Calling the password_gen() function with default parameters:

```python
passwrd = password_gen()
print(f'->> Password with default function: "{passwrd}"')
```

### Output

```shell
Terminal$ python3 universally_unique_id_gen.py 
->> Password with default function: "Sb429#U"
```


### Calling the password_gen() function with specified lenght and a default alphabet parameters:

```python
lenght = 15
passwrd = password_gen(lenght)
print(f'->> Password with function with lenght of {lenght}: "{passwrd}"')
```

### Output

```shell
Terminal$ python3 universally_unique_id_gen.py 
->> Password with function with lenght of 15: "0SsX~xYFSIVHo7Z"
```


---
# Password Generator.

Pending.



