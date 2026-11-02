
# Function to perform Hill Cipher encryption
def hillCipher(text, keyMatrix):

    result = ""

    # Remove spaces and convert text to uppercase
    text = text.upper().replace(" ", "")

    # Check whether text length is even
    if len(text) % 2 != 0:
        return "Text length must be even!"

    # Process two characters at a time
    for i in range(0, len(text), 2):

        # Convert characters into numbers
        p1 = ord(text[i]) - ord("A")
        p2 = ord(text[i + 1]) - ord("A")

        # Matrix multiplication
        c1 = (keyMatrix[0][0] * p1 +
              keyMatrix[0][1] * p2) % 26

        c2 = (keyMatrix[1][0] * p1 +
              keyMatrix[1][1] * p2) % 26

        # Convert numbers back into characters
        result += chr(c1 + ord("A"))
        result += chr(c2 + ord("A"))

    return result



text = input("Enter the plaintext: ")

# Define 2x2 key matrix
keyMatrix = [
    [3, 3],
    [2, 5]
]

print("\nKey Matrix:")
for row in keyMatrix:
    print(row)

encrypted = hillCipher(text, keyMatrix)

print("\nEncrypted text:", encrypted)

print("================================")
