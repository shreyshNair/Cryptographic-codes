
# Buffer Overflow Attack Demonstration

# Define buffer size
BUFFER_SIZE = 8

# Create a fixed-size buffer
buffer = bytearray(BUFFER_SIZE)

# Get user input
userInput = input("Enter data: ")

# Convert input into bytes
data = userInput.encode()

print("\nBuffer Size:", BUFFER_SIZE)
print("Input Size:", len(data))

# Demonstrate vulnerable behaviour conceptually
if len(data) > BUFFER_SIZE:

    print("\nBuffer Overflow Detected!")
    print("Input exceeds allocated buffer capacity.")

else:

    # Copy data into buffer
    buffer[:len(data)] = data

    print("\nData stored successfully!")
    print("Buffer Content:", buffer)

# Secure implementation
print("\n--- Secure Implementation ---")

if len(data) <= BUFFER_SIZE:

    safeBuffer = bytearray(BUFFER_SIZE)
    safeBuffer[:len(data)] = data

    print("Input accepted safely.")

else:

    print("Input rejected due to size limit.")

