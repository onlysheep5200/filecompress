#-*- coding:utf-8 -*-
__author__ = 'mac'
from Crypto.Cipher import AES

BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

class Compressor(object) :
    def __init__(self,encryptor = None):
        self.compressed = {}
        self.encryptor = encryptor

    def compress(self,path):
        with open(path,'r+') as f :
            content = f.read()
            if self.encryptor :
                content = self.encryptor.encrypt(content)
            self.compressed[path] = content

    def dump(self,target = "compressed.cms"):
        if self.compressed :
            with open(target,'w') as f :
                for key,value in self.compressed.items() :
                    val = key+'-'+value
                    if self.encryptor :
                        val = self.encryptor.encrypt(val)
                    f.write(val+',')