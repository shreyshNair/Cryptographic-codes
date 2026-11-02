
import hashlib
import secrets

# Secret pepper stored separately from the password database
PEPPER = "MySecretPepper123"


# Function to generate salted and peppered password hash
def hashPassword(password):

    # Generate a random salt
    salt = secrets.token_hex(16)

    # Combine password, salt and pepper
    combined = password + salt + PEPPER

    # Generate SHA-256 hash
    password_hash = hashlib.sha256(
        combined.encode()
    ).hexdigest()

    return salt, password_hash


# Function to verify password
def verifyPassword(password, salt, stored_hash):

    # Combine entered password with original salt and pepper
    combined = password + salt + PEPPER

    # Generate hash again
    new_hash = hashlib.sha256(
        combined.encode()
    ).hexdigest()

    # Compare generated hash with stored hash
    return secrets.compare_digest(new_hash, stored_hash)

password = input("Enter your password: ")

# Generate password hash
salt, stored_hash = hashPassword(password)

print("\nGenerated Salt:", salt)
print("Stored Password Hash:", stored_hash)

# Verify password
entered_password = input("\nRe-enter your password: ")

if verifyPassword(entered_password, salt, stored_hash):
    print("Password verification successful!")

else:
    print("Incorrect password!")

