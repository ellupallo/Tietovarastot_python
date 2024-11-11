# pip install bcrypt
import bcrypt

password = "qwerty123" # tää on se salasana

# convert password to byte array:
password_as_bytes = password.encode("utf-8") # uft-8 on oletus, voisi olla myös encode()
# generate the salt
salt = bcrypt.gensalt()
print(salt)

# hash the password using salt
hash = bcrypt.hashpw(password_as_bytes, salt)
print(hash)

# check if password is correct
result = bcrypt.checkpw(password_as_bytes,hash) # True or False
print(result)