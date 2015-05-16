# dj-secret-key-util
###Overview
Generates a secret key and saves it into a file. The secret key can also be set as environment variable `SECRET_KEY`.  

###Usage
######In Django
    from secret_key_util import get_secret_key
    SECRET_KEY = get_secret_key()
