
def modinverse(key):
    for i in range(1, 26):
        if (key * i) % 26 == 1:
            return i
    return None


def mmultiplicativeCipher(text, key, mode):

    result = ""

    inverse = modinverse(key)

    for char in text:

        if char.isalpha():

            char = char.upper()

            p = ord(char) - ord("A")

            if mode == "E":
                c = (p * key) % 26

            else:
                c = (p * inverse) % 26

            result += chr(c + ord("A"))

        else:
            result += char

    return result


text = input("Enter the text: ")

key = int(input("Enter the key: "))

key = key % 26

inverse = modinverse(key)

if inverse is None:

    print("Invalid key! Enter a key coprime with 26.")

else:

    print("1. Encryption")
    print("2. Decryption")

    choice = input("Enter your choice: ")

    if choice == "1":

        encryption = mmultiplicativeCipher(text, key, "E")

        print("Encrypted text:", encryption)

    elif choice == "2":

        decryption = mmultiplicativeCipher(text, key, "D")

        print("Decrypted text:", decryption)

    else:
        print("Invalid choice")
