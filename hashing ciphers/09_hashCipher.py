
import hashlib
import time
#to generate 1kb file: python3 -c "open('sample.txt', 'w').write('A' * 1024)"
# Open and read the text file in binary mode
with open("sample.txt", "rb") as file:
    data = file.read()

# Calculate MD5 hash
start = time.time()

md5_hash = hashlib.md5(data).hexdigest()

md5_time = time.time() - start

# Calculate SHA-1 hash
start = time.time()

sha1_hash = hashlib.sha1(data).hexdigest()

sha1_time = time.time() - start

# Display the results

print("\nMD5 Hash:")
print(md5_hash)

print("\nSHA-1 Hash:")
print(sha1_hash)

print("\nExecution Time:")

print("MD5 Time:", md5_time, "seconds")
print("SHA-1 Time:", sha1_time, "seconds")


