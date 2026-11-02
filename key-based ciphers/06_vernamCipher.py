def vernamCipher(text,key):
    result = ""

    if len(text)!=len(key):
        return None

    for i in range(len(text)):
        p = ord(text[i])
        #k = ord(key[i % len(key)]) use this instead below if the key size and plaintext are not supposed to match
        k = ord(key[i])
        c = p ^ k
        result += chr(c)
    return result

text= input("enter the text:")
key= input("enter the key:")

if len(text) != len(key):
    print("the k=length of the key and plaintext dont match")

else:
    encrypted = vernamCipher(text , key)
    print("encryptedd text is: " ,repr(encrypted))

    decrypted = vernamCipher(encrypted, key)
    print  ("decrypted text is: ", repr(decrypted))
