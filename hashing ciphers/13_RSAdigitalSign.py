
# RSA Digital Signature

import hashlib


# Function to calculate GCD
def gcd(a, b):

    while b != 0:
        a, b = b, a % b

    return a


# Function to find modular inverse
def modInverse(e, phi):

    for d in range(1, phi):

        if (e * d) % phi == 1:
            return d

    return None


# Function to generate hash of message
def generateHash(message):

    hashValue = hashlib.sha256(message.encode()).hexdigest()

    return int(hashValue, 16)

# RSA key generation
p = 3
q = 11

n = p * q
phi = (p - 1) * (q - 1)

e = 3
d = modInverse(e, phi)

# Display keys
print("Public Key:", (e, n))
print("Private Key:", (d, n))

# Enter message
message = input("\nEnter the message: ")

# Generate message hash
messageHash = generateHash(message)

# Generate digital signature using private key
signature = pow(messageHash, d, n)

print("\nOriginal Message:", message)
print("Message Hash:", messageHash)
print("Digital Signature:", signature)

# Verify signature using public key
verifiedHash = pow(signature, e, n)

# Compare the hashes modulo n
if verifiedHash == messageHash % n:

    print("\nDigital Signature Verified Successfully!")

else:

    print("\nDigital Signature Verification Failed!")

