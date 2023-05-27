from cryptography.fernet import Fernet


class Crypt:
    __path_key = 'crypto.key'

    def __init__(self, path: str):
        self.path = path
        if self._load_key() == b'':
            self._write_key()

    def _write_key(self):
        key = Fernet.generate_key()
        with open(self.__path_key, 'wb') as file:
            file.write(key)

    def _load_key(self):
        return open(self.__path_key, 'rb').read()

    def _encrypt(self, filename, key):
        f = Fernet(key)

        with open(filename, 'rb') as file:
            file_data = file.read()
            encrypt_data = f.encrypt(file_data)

        with open(filename, 'wb') as file:
            file.write(encrypt_data)


    def _decrypt(self, file, key):
        f = Fernet(key)

        with open(self.path, 'rb') as file:
            file_data = file.read()
            decrypt_data = f.decrypt(file_data)

        with open(self.path, 'wb') as file:
            file.write(decrypt_data)

    def encrypt_file(self):
        self._encrypt(self.path, self._load_key())

    def decrypt_file(self):
        self._decrypt(self.path, self._load_key())

if __name__ == '__main__':
    a = Crypt('test file.txt')
    a.encrypt_file()
    #a.decrypt_file()
