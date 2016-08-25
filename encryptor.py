#-*- coding:utf-8
__author__ = 'mac'
from Crypto.Cipher import AES
import base64

class AesEncryptor(object) :

    def __init__(self,key):
        self.encryptor = AES.new(key,AES.MODE_CBC,b'0000000000000000')
        BS = AES.block_size
        self.pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        self.unpad = lambda s : s[0:-ord(s[-1])]


    def encrypt(self,content):
        encrypted = self.encryptor.encrypt(self.pad(content))
        return base64.encode(encrypted)

    def decrypt(self,contet):
        return self.unpad(self.encryptor.decrypt(base64.decode(contet)))