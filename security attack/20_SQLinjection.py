
# SQL Injection Attack Demonstration

import sqlite3

# Create an in-memory database
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Create users table
cursor.execute("""
CREATE TABLE users (
    username TEXT,
    password TEXT
)
""")

# Insert sample users
cursor.execute(
    "INSERT INTO users VALUES (?, ?)",
    ("admin", "admin123")
)

cursor.execute(
    "INSERT INTO users VALUES (?, ?)",
    ("user", "user123")
)

conn.commit()

print("================================")
print("     SQL INJECTION DEMO")
print("================================")

# Get login details
username = input("Enter username: ")
password = input("Enter password: ")

# Vulnerable SQL query
query = (
    "SELECT * FROM users WHERE username = '"
    + username
    + "' AND password = '"
    + password
    + "'"
)

print("\nVulnerable Query:")
print(query)

# Execute vulnerable query
cursor.execute(query)
result = cursor.fetchone()

if result:
    print("\nVulnerable Login: Successful!")
else:
    print("\nVulnerable Login: Failed!")

# Secure SQL query using parameters
safeQuery = """
SELECT * FROM users
WHERE username = ? AND password = ?
"""

cursor.execute(safeQuery, (username, password))
safeResult = cursor.fetchone()

if safeResult:
    print("Secure Login: Successful!")
else:
    print("Secure Login: Failed!")

# Close database connection
conn.close()

