__author__ = 'mac'
from Crypto.Cipher import AES
import sys
from encryptor import AesEncryptor

if len(sys.argv) < 4 :
    print "need at least a argument"
    exit()




if __name__ == '__main__' :
    op = sys.argv[1]
    key = sys.argv[2]
    posix = sys.argv[3]
    path = sys.argv[4]
    mode = AES.MODE_CBC

    try:
        encryptor = AesEncryptor(key)
    except Exception,e :
        print e.message
        exit()
