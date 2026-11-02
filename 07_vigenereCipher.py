
def vigenereCipher(text, key, mode):

    result = ""

    j = 0
    key = key.upper()

    for char in text:

        if char.isalpha():

            char = char.upper()

            p = ord(char) - ord("A")

            k = ord(key[j % len(key)]) - ord("A")

            if mode == "E":

                c = (p + k) % 26

            else:

                c = (p - k) % 26

            result += chr(c + ord("A"))

            j += 1

        else:

            result += char

    return result


text = input("Enter the text: ")
key = input("Enter the key: ")

if len(key) == 0 or not key.isalpha():

    print("Invalid key! Enter alphabets only.")

else:

    print("1. Encryption")
    print("2. Decryption")

    choice = input("Enter your choice: ")

    if choice == "1":

        encrypted = vigenereCipher(text, key, "E")

        print("Encrypted text:", encrypted)

    elif choice == "2":

        decrypted = vigenereCipher(text, key, "D")

        print("Decrypted text:", decrypted)

    else:

        print("Invalid choice")
