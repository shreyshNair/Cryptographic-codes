
# Diffie-Hellman Key Exchange

# Public values
p = int(input("Enter a prime number (p): "))
g = int(input("Enter the generator (g): "))

# Alice's private key
a = int(input("Enter Alice's private key: "))

# Bob's private key
b = int(input("Enter Bob's private key: "))

# Calculate Alice's public key
A = pow(g, a, p)

# Calculate Bob's public key
B = pow(g, b, p)

# Calculate shared secret for Alice
keyAlice = pow(B, a, p)

# Calculate shared secret for Bob
keyBob = pow(A, b, p)

# Display results

print("Alice's Public Key:", A)
print("Bob's Public Key:", B)

print("Alice's Shared Key:", keyAlice)
print("Bob's Shared Key:", keyBob)

# Verify whether both keys are equal
if keyAlice == keyBob:
    print("\nShared secret established successfully!")

else:
    print("\nKey exchange failed!")


