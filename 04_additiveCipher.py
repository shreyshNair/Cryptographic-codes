def additiveCipher(text, key , mode):
    result = ""
    for char in text:
        if char.isalpha():
            char = char.upper()

            p = ord(char) - ord("A")

            if mode == "E":
                c = (p + key)%26
            else:
                c = (p - key)%26

            result += chr(c + ord("A"))
        else:
            result += char
    return result

text=input("enter the text:")
key= int(input("enter the key:"))
key = key%26

print("1. ecryption")
print("2. decryption")

choice = input("enter your choice")

if choice == "1":
    encryption = additiveCipher(text , key , "E")
    print(encryption)
elif choice == "2":
    decryption = additiveCipher(text, key , "D")
    print(decryption)
else:
    print("invalid choice")