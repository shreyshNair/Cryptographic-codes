
def shiftcipher(text , key , mode):
    result = ""
    for char in text:
        if char.isalpha():
            char = char.upper()
            p= ord(char)- ord("A")

            if mode == "E":
                c = ( p + key)%26
            else:
                c = (p - key)%26
#chr: below block is used to convert alphabet into numeric value
            result += chr(c+ ord("A"))
        else:
            result += char

    return result



text = input("enter your text:")
key = int(input("enter your key:"))
key = key%26

print("1. encryption")
print("2. decryption")

choice = (input("enter your choice"))

if choice == "1":
    encrypted = shiftcipher(text , key , "E")
    print("Encrypted Text is: ", encrypted)
elif choice == "2":
    decrypted = shiftcipher(text, key , 'D')
    print("Decrypted Text is: " , decrypted)
else:
    print("Invalid choice")