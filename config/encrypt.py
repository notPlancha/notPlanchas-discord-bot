import sys
import os
import getpass
from pyAesCrypt import encryptFile as encrypt

# args should be 'file password'
args = sys.argv
if len(args) < 3:
    if len(args) == 1:
        args.append(input("File to encrypt: "))
    args.append(getpass.getpass("Password: "))
encrypt(args[1], args[1] + ".aes", args[2], bufferSize=64 * 1024, )
print("Encrypted file: " + args[1] + ".aes")
