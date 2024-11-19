# Madison Manning
# UWYO COSC 1010
# 10/19/2024
# Lab 10
# Lab Section: 10
# Sources, people worked with, help given to: Special thanks to Paige and Eric

#import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()


# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.

hash_string = ""
hash_text = ""
password = ""
password_found = False

try:
    imp_hash = Path("hash")
    hash_text = imp_hash.read_text()
except:
    print(f"Hash not found, please upload")
else:
    pass

try:
    imp_path = Path("rockyou.txt")
    imp_prompt = imp_path.read_text()
    passes = imp_prompt.splitlines()
except:
    print(f"File not found, try again")
else:
    for string in passes:
        hash_string = get_hash(string)
        if hash_string == hash_text:
            password = string
            password_found = True
            break
        else:
            pass
finally:
    if password_found == True:
        print(f"The password is {password}")
    else:
        print(f"The password could not be found")


