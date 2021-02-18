import pyopenssl
import base64
from Crypto.PublicKey import RSA
from os import path

def symetric_keygen(as_base64):
    key = os.urandom(32)
    encoded_key = base64.b64encode(key).decode("utf-8")
    
    print("Base 64 encoded encryption key: {}".format(encoded_key))
    print("\n", "unencodedkey", key)

def import_publickey():
    public_key_path = input('please provide they key path':)
    Crypto.PublicKey.RSA.import_key(public_key_path, passphrase=None)

def create_wrapped_key(with_public_key):
    wrap
    plaintext = key
    secret = b'*Thirty-two byte (256 bits) key*'
    cipher = Salsa20.new(key=secret)
    msg = cipher.nonce + cipher.encrypt(plaintext)

    

#stuff I want done in python instead of bash
#"${OPENSSL_V110}" rsautl \
#   -encrypt \
#   -pubin \
#   -inkey "${PUB_WRAPPING_KEY}" \ #let it prompt for the public key of google cloud
#   -in "${TEMP_AES_KEY}" \ #take the just generated key as input
#   -out "${TEMP_AES_KEY_WRAPPED}" \ #send it out to a location prompt the user for a keyname
#   -oaep #pad it with SHA1
#
#

# Wrap the target key with the temporary AES key using the CKM_AES_KEY_WRAP_PAD algorithm. 
# Replace target-key-file with the name of the .bin or pub file for the key.
# The -iv A65959A6 flag sets A65959A6 as the Alternate Initial Value. This is required by the RFC 5649 specification.
#"${OPENSSL_V110}" enc \
#  -id-aes256-wrap-pad \
#  -iv A65959A6 \
#  -K $( hexdump -v -e '/1 "%02x"' < "${TEMP_AES_KEY}" ) \
#  -in "${TARGET_KEY}" \
#  -out "${TARGET_KEY_WRAPPED}"



def encrypt(message, public_key_pem_path):
    # set public key path 
    public_key_path = '/test.pub'
    public_key = RSA.importKey(open(public_key_path, 'r').read())
    # creating the RSA object using public key
    rsa_object = PKCS1_v1_5.new(public_key)
    cipher_text = rsa_object.encrypt(message.encode())
    cipher_text = base64.b64encode(cipher_text)
    return cipher_text
    public_key = RSA.importKey(open(public_key_path, 'r').read())
    rsa_object = PKCS1_v1_5.new(public_key)
    cipher_text = rsa_object.encrypt(message.encode())
    cipher_text = base64.b64encode(cipher_text)
    return cipher_text

