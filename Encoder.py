import base64
import binascii
import hashlib
from cryptography.fernet import Fernet

#take words
asker = input("Type what you want to encode: ")

list_of_types = 'base64, hex, md5, sha256, base85, sha512, base16, sha1, base32'
print(list_of_types)

ask_type = input("what type of encode you want?: ")


#functionality

if ask_type == 'base64':
    base64_encoder = base64.b64encode(asker.encode())
    print(base64_encoder)
elif ask_type == 'hex':
    hex_encoder = binascii.hexlify(asker.encode())
    print(hex_encoder)
elif ask_type == 'md5':
    hash_encoder = hashlib.md5(asker.encode()).hexdigest()
    print(hash_encoder)
elif ask_type == 'sha256':
    sha256_encoder = hashlib.sha256(asker.encode())
    print(sha256_encoder)
elif ask_type == 'base85':
    base85_encoder = base64.b85decode(asker.encode())
    print(base85_encoder)
elif ask_type == 'sha512':
    sha512_encoder = hashlib.sha512(asker.encode())
    print(sha512_encoder)
elif ask_type == 'base16':
    base16_encoder = base64.b16encode(asker.encode())
    print(base16_encoder)
elif ask_type == 'sha1':
    sha1_encoder = hashlib.sha1(asker.encode())
    print(sha1_encoder)
elif ask_type == 'base32':
    base32_encoder = base64.b32encode(asker.encode())
    print(base32_encoder)                
else:
    print('invalid type!')    
