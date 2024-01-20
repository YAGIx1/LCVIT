
def xor_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])

def encrypt_pass(plaintext, key):
    encrypted_text = ""

    for char in plaintext:
        if char.isnumeric():
            # If the character is a number, shift it by the key value
            encrypted_char = str((int(char) + key) % 10)
            encrypted_text += encrypted_char
        else:
            # If the character is not a number, leave it unchanged
            encrypted_text += char

    return encrypted_text


def decrypt_pass(ciphertext, key):
    decrypted_text = ""

    for char in ciphertext:
        if char.isnumeric():
            # If the character is a number, shift it by the key value
            decrypted_char = str((int(char) - key) % 10)
            decrypted_text += decrypted_char
        else:
            # If the character is not a number, leave it unchanged
            decrypted_text += char

    return decrypted_text



flag_enc = open('flag.txt.enc', 'rb').read()



def pass_check():
    user_pw = input("Please enter correct password for flag: ")
    
    if( user_pw == decrypt_pass("69043",2) ):
        print("FLAG:")
        decryption = xor_xor(flag_enc.decode(), "linuxclub")
        print(decryption)
        return
    print("That password is incorrect")



pass_check()
