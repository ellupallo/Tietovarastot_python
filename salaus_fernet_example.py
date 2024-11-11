# Fernet module is imported from the  
# cryptography package eli pip install cryptography
from cryptography.fernet import Fernet 
  
# key is generated 
key = Fernet.generate_key() 
# value of key is assigned to a variable 
f = Fernet(key) 
# the plaintext is converted to ciphertext 
token = f.encrypt(b"welcome to geeksforgeeks") 

# ************************************************
# TOINEN VAIHTOEHTO
# pw = "JOULU"
# token = f.encrypt(pw.encode("utf-8"))
# ************************************************
# display the ciphertext 
print(token) 
  
# decrypting the ciphertext 
secret = f.decrypt(token) 
# display the plaintext 
print(secret) 

# kryptauksen tallennus ja samalla koodilla myös lukeminen
with open("salaus-fernet_token_crypted.bin", "wb") as file: # =wb= write as binary, rb = read as binary
    file.write(token) # tulee file
