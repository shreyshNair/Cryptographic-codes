def evenOddCipher(text, mode):
    result = ""

    if mode == "E":
        even = text[1::2]
        odd = text[0::2]

        result = even + odd

    else:

        even_count = len(text) //2
        even = text[:even_count]
        odd = text[even_count:]

        for i in range(len(odd)):
            result += odd[i]

            if i < len(even):
                result += even[i]

    return result

text = input("Enter the text: ")

print("\n1. Encryption")
print("2. Decryption")

choice = input("Enter your choice: ")

if choice == "1":
    encrypted = evenOddCipher(text, "E")
    print("Encrypted text:", encrypted)

elif choice == "2":
    decrypted = evenOddCipher(text, "D")
    print("Decrypted text:", decrypted)

else:
    print("Invalid choice")