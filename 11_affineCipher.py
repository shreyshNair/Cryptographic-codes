# Function to find the modular multiplicative inverse
def modInverse(a):
    for i in range(1, 26):
        if (a * i) % 26 == 1:
            return i
    return None


# Function to perform Affine Cipher
def affineCipher(text, a, b, mode):
    result = ""

    # Find the modular inverse of a
    inverse = modInverse(a)

    for char in text:
        if char.isalpha():
            char = char.upper()

            # Convert character into a number (A=0, B=1, ..., Z=25)
            p = ord(char) - ord("A")

            if mode == "E":
                # Encryption: C = (aP + b) mod 26
                c = (a * p + b) % 26
            else:
                # Decryption: P = a_inverse * (C - b) mod 26
                c = (inverse * (p - b)) % 26

            # Convert number back into a character
            result += chr(c + ord("A"))

        else:
            # Preserve spaces and special characters
            result += char

    return result

text = input("Enter the text: ")

a = int(input("Enter multiplicative key (a): "))
b = int(input("Enter additive key (b): "))

# Keep keys within the range 0-25
a = a % 26
b = b % 26

# Check whether the multiplicative key is valid
if modInverse(a) is None:
    print("Invalid key! 'a' must be coprime with 26.")

else:
    print("\n1. Encryption")
    print("2. Decryption")

    choice = input("Enter your choice: ")

    if choice == "1":
        encrypted = affineCipher(text, a, b, "E")
        print("Encrypted text:", encrypted)

    elif choice == "2":
        decrypted = affineCipher(text, a, b, "D")
        print("Decrypted text:", decrypted)

    else:
        print("Invalid choice")


