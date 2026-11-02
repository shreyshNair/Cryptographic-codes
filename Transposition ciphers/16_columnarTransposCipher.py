
# Function to perform Columnar Transposition Cipher
def columnarCipher(text, columns, mode):

    result = ""

    # Encryption
    if mode == "E":

        # Read characters column by column
        for col in range(columns):

            for i in range(col, len(text), columns):
                result += text[i]

    # Decryption
    else:

        # Calculate number of rows
        rows = (len(text) + columns - 1) // columns

        # Calculate characters in each column
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

text = input("Enter the text: ")

columns = 4

print("\nNumber of columns:", columns)
print("1. Encryption")
print("2. Decryption")

choice = input("Enter your choice: ")

if choice == "1":
    encrypted = columnarCipher(text, columns, "E")
    print("Encrypted text:", encrypted)

elif choice == "2":
    decrypted = columnarCipher(text, columns, "D")
    print("Decrypted text:", decrypted)

else:
    print("Invalid choice")

print("================================")
