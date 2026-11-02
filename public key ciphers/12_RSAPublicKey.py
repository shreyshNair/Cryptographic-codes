
# Function to find GCD
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


# Function to check whether a number is prime
def isPrime(n):

    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            return False

    return True


# Enter two prime numbers
p = int(input("Enter first prime number: "))
q = int(input("Enter second prime number: "))

# Validate prime numbers
if not isPrime(p) or not isPrime(q) or p == q:

    print("Enter two distinct prime numbers!")

else:

    # Calculate n
    n = p * q

    # Calculate Euler's Totient
    phi = (p - 1) * (q - 1)

    # Select public exponent
    e = 2

    while e < phi:

        if gcd(e, phi) == 1:
            break

        e += 1

    # Calculate private exponent
    d = modInverse(e, phi)

    # Display keys
    print("\nPublic Key:", (e, n))
    print("Private Key:", (d, n))

    # Enter plaintext as a number
    message = int(input("\nEnter message (number): "))

    if message < 0 or message >= n:

        print("Message must be between 0 and", n - 1)

    else:

        # Encryption
        encrypted = pow(message, e, n)

        # Decryption
        decrypted = pow(encrypted, d, n)

        print("\nEncrypted Message:", encrypted)
        print("Decrypted Message:", decrypted)

