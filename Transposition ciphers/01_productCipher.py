
# Function to perform Additive Substitution Cipher
def substitutionCipher(text, key, mode):

    result = ""

    for char in text:

        if char.isalpha():

            char = char.upper()

            # Convert character into a number
            p = ord(char) - ord("A")

            if mode == "E":
                # Encryption
                c = (p + key) % 26

            else:
                # Decryption
                c = (p - key) % 26

            # Convert number back into a character
            result += chr(c + ord("A"))

        else:
            result += char

    return result


# Function to perform Columnar Transposition
def transpositionCipher(text, columns, mode):

    result = ""

    if mode == "E":

        # Read characters column by column
        for col in range(columns):

            for i in range(col, len(text), columns):
                result += text[i]

    else:

        # Calculate number of rows
        rows = (len(text) + columns - 1) // columns

        # Calculate length of each column
        column_lengths = []

        for col in range(columns):
            length = len(range(col, len(text), columns))
            column_lengths.append(length)

        # Divide ciphertext into columns
        matrix = []
        start = 0

        for length in column_lengths:
            matrix.append(text[start:start + length])
            start += length

        # Reconstruct original text row by row
        for row in range(rows):

            for col in range(columns):

                if row < len(matrix[col]):
                    result += matrix[col][row]

    return result


# Function to perform Product Cipher
def productCipher(text, key, columns, mode):

    if mode == "E":

        # First perform substitution
        substituted = substitutionCipher(text, key, "E")

        # Then perform transposition
        encrypted = transpositionCipher(substituted, columns, "E")

        return encrypted

    else:

        # First reverse transposition
        transposed = transpositionCipher(text, columns, "D")

        # Then reverse substitution
        decrypted = substitutionCipher(transposed, key, "D")

        return decrypted




text = input("Enter the text: ")

key = int(input("Enter the substitution key: "))
key = key % 26

columns = 4

print("\nNumber of columns:", columns)
print("1. Encryption")
print("2. Decryption")

choice = input("Enter your choice: ")

if choice == "1":

    encrypted = productCipher(text, key, columns, "E")

    print("Encrypted text:", encrypted)

elif choice == "2":

    decrypted = productCipher(text, key, columns, "D")

    print("Decrypted text:", decrypted)

else:

    print("Invalid choice")


