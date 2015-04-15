import os
import random

SECRET_KEY_FILE_PATH = os.path.expanduser("~/.secret_key")
SECRET_KEY_CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

MSG_KEY_NOT_SET = "SECRET_KEY was not set. Generated a new Secret Key."


def get_secret_key():
    """
    Reads the secret key as environment variable or generate it when it's not present.
    :return: the secret key
    """
    key = os.environ.get("SECRET_KEY", None)
    if key is None:
        if os.path.isfile(SECRET_KEY_FILE_PATH):
            # file exists, read the key
            with open(SECRET_KEY_FILE_PATH, "r") as secret_key_file:
                key = secret_key_file.read()
                return str(key)

        # the key isn't set yet - a new one will be created
        print(MSG_KEY_NOT_SET)
        chars = SECRET_KEY_CHARS
        key = ''.join(random.choice(chars) for _ in range(50))
        with open(SECRET_KEY_FILE_PATH, "w+") as secret_key_file:
            secret_key_file.write(key)
    return str(key)