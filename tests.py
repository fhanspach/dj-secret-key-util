import unittest
from secret_key_util import SecretKeyUtil


class TestKeyStore(object):
    def __init__(self):
        self.test_key = ""


key_store = TestKeyStore()


class TestSecretKey(unittest.TestCase):
    @staticmethod
    def write_key_mock(key):
        key_store.test_key = key

    @staticmethod
    def read_key_mock():
        return key_store.test_key

    def mock_methods(self):
        SecretKeyUtil.read_key = TestSecretKey.read_key_mock
        SecretKeyUtil.write_key = TestSecretKey.write_key_mock
        SecretKeyUtil.key_file_present = lambda: key_store.test_key != ""
        print("key file present: {}".format(SecretKeyUtil.key_file_present()))

    def test_generate_new_key(self):
        self.mock_methods()
        self.assertTrue(SecretKeyUtil.get_secret_key())

    def test_use_old_key(self):
        key_store.test_key = "n4bl4"
        self.mock_methods()
        print(key_store.test_key)
        self.assertEqual('n4bl4', SecretKeyUtil.get_secret_key())

    def test_generated_key_stays(self):
        self.mock_methods()
        key = SecretKeyUtil.get_secret_key()
        self.assertNotEqual("", key)
        self.assertEqual(key, SecretKeyUtil.get_secret_key())

    def test_defined_env_key(self):
        import os
        KEY = "N4BLA"
        os.environ["SECRET_KEY"] = KEY
        key = SecretKeyUtil.get_secret_key()
        self.assertEqual(key, KEY)
        del os.environ["SECRET_KEY"]
