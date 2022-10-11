import sys
import os
import getpass
from pyAesCrypt import decryptFile as decrypt

# args should be 'file password'
args = sys.argv
if len(args) < 3:
    if len(args) == 1:
        args.append(input("File to decrypt: "))
    args.append(getpass.getpass("Password: "))
decrypt(args[1], args[1][:-4], args[2], bufferSize=64 * 1024)
print("Decrypted file: " + args[1][:-4])
