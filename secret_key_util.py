import os
from random import random


def get_secret_key():
    """
    Reads the secret key as environment variable or generate it when it's not present.
    :return: the secret key
    """
    key = os.environ.get("SECRET_KEY", None)
    if key is None:
        print("SECRET_KEY was not set. Generated a new Secret Key.")
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.choice(chars) for _ in range(50))
    return str(key)
