
# Man-in-the-Middle Attack in Diffie-Hellman

# Public values
p = 23
g = 5

# Alice and Bob private keys
a = 6
b = 15

# Attacker's private keys
x = 13
y = 9

# Alice and Bob public keys
A = pow(g, a, p)
B = pow(g, b, p)

# Attacker generates two public keys
X = pow(g, x, p)
Y = pow(g, y, p)

# Attacker intercepts and replaces public keys

# Alice receives attacker's public key X
# Bob receives attacker's public key Y

# Alice calculates shared key with attacker
keyAlice = pow(X, a, p)

# Bob calculates shared key with attacker
keyBob = pow(Y, b, p)

# Attacker calculates shared key with Alice
keyAttackerAlice = pow(A, x, p)

# Attacker calculates shared key with Bob
keyAttackerBob = pow(B, y, p)

# Display results
print("================================")
print("     DIFFIE-HELLMAN MITM ATTACK")
print("================================")

print("Alice's Public Key:", A)
print("Bob's Public Key:", B)

print("\nAttacker's Public Key for Alice:", X)
print("Attacker's Public Key for Bob:", Y)

print("\nAlice's Shared Key:", keyAlice)
print("Attacker's Key with Alice:", keyAttackerAlice)

print("\nBob's Shared Key:", keyBob)
print("Attacker's Key with Bob:", keyAttackerBob)

# Verify attack
if keyAlice == keyAttackerAlice and keyBob == keyAttackerBob:
    print("\nMITM Attack Successful!")
else:
    print("\nMITM Attack Failed!")

print("================================")
