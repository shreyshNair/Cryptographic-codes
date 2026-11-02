
# Practical 8: Playfair Cipher
# Implementing only Same Row and Same Column rules

# Function to generate the 5x5 Playfair matrix
def generateMatrix(key):

    key = key.upper().replace("J", "I")

    matrix = []
    used = ""

    # Add unique characters from the key
    for char in key:
        if char.isalpha() and char not in used:
            used += char

    # Add remaining alphabets
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used:
            used += char

    # Convert the string into a 5x5 matrix
    for i in range(0, 25, 5):
        matrix.append(list(used[i:i+5]))

    return matrix


# Function to find the position of a character
def findPosition(matrix, char):

    for i in range(5):
        for j in range(5):

            if matrix[i][j] == char:
                return i, j

    return None


# Function to encrypt a pair of characters
def encryptPair(matrix, a, b):

    row1, col1 = findPosition(matrix, a)
    row2, col2 = findPosition(matrix, b)

    # Rule 1: Same row
    if row1 == row2:

        col1 = (col1 + 1) % 5
        col2 = (col2 + 1) % 5

    # Rule 2: Same column
    elif col1 == col2:

        row1 = (row1 + 1) % 5
        row2 = (row2 + 1) % 5

    else:

        return None

    return matrix[row1][col1] + matrix[row2][col2]


# Function to encrypt the complete plaintext
def playfairCipher(text, key):

    matrix = generateMatrix(key)

    # Convert text to uppercase and replace J with I
    text = text.upper().replace("J", "I")

    # Keep only alphabetic characters
    text = "".join(char for char in text if char.isalpha())

    result = ""

    # Process two characters at a time
    if len(text) % 2 != 0:
        text += "X"

    for i in range(0, len(text), 2):

        a = text[i]
        b = text[i+1]

        encrypted = encryptPair(matrix, a, b)

        if encrypted is None:
            return "Pair " + a + b + " requires the rectangle rule."

        result += encrypted

    return result


# Main program

print("================================")
print("        PLAYFAIR CIPHER")
print("================================")

text = input("Enter the plaintext: ")
key = input("Enter the key: ")

if not key.isalpha():

    print("Invalid key! Enter alphabets only.")

else:

    encrypted = playfairCipher(text, key)

    print("Encrypted text:", encrypted)

print("================================")
