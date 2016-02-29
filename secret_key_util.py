import os
import random
import sys

SECRET_KEY_FILE_PATH = os.path.expanduser("~/.secret_key")
SECRET_KEY_CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

MSG_KEY_NOT_SET = "SECRET_KEY was not set. Generated a new Secret Key."


class SecretKeyUtil(object):
    @staticmethod
    def generate_key(chars):
        return ''.join(random.choice(chars) for _ in range(50))

    @staticmethod
    def get_secret_key():
        """
        Reads the secret key from file system or generates it when it's not present.
        :return: the secret key
        """
        if SecretKeyUtil.key_file_present():
            # file exists, read the key
            return SecretKeyUtil.read_key()
        # the key isn't set yet - a new one will be created
        print(MSG_KEY_NOT_SET)
        chars = SECRET_KEY_CHARS
        key = SecretKeyUtil.generate_key(chars)
        SecretKeyUtil.write_key(key)
        return SecretKeyUtil.read_key()

    @staticmethod
    def write_key(key):
        with open(SECRET_KEY_FILE_PATH, "w+") as secret_key_file:
            secret_key_file.write(key)

    @staticmethod
    def read_key():
        with open(SECRET_KEY_FILE_PATH, "r") as secret_key_file:
            key = secret_key_file.read()
            return str(key)

    @staticmethod
    def key_file_present():
        return os.path.isfile(SECRET_KEY_FILE_PATH)


if __name__ == '__main__':
    if "--generate" in sys.argv or "-g" in sys.argv:
        print("New secret key: " + SecretKeyUtil.generate_key(SECRET_KEY_CHARS))
    else:
        print(SecretKeyUtil.get_secret_key())


def get_secret_key():
    return SecretKeyUtil.get_secret_key()
