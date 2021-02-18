import base64
import os
import tkinter as tk
from tkinter import filedialog
import rsa



key = os.urandom(32)
encoded_key = base64.b64encode(key).decode("utf-8")
    
print("Base 64 encoded encryption key: {}".format(encoded_key))
print("\n", key)
print("please select GCP provided public key")

gcp_key_file = (input "Location: ")
message = encoded_key
public_key = gcp_key_file
encrypted_message = rsa.encrypt(message, public_key)
print(encrypted_message, decrypted_message, sep="\n\n")

with open(input("relative or public filepath"), 'rU') as input_file:
    #encode the key string with the input_file  as publickey
    #4096 bits RSA - OAEP - SHA1 Digest - 256 BIT AES-KWP
    pub_key = input_file
    #RSA.import(pub_key)
    









