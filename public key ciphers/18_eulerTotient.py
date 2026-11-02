
import math

# Function to calculate Euler's Totient Function
def eulerTotient(n):

    # Rule 1: If n is 1
    if n == 1:
        return 1

    # Rule 2: If n is prime
    isPrime = True

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            isPrime = False
            break

    if isPrime:
        return n - 1

    # Rule 3: Find two coprime factors
    for m in range(2, n):

        if n % m == 0:

            p = n // m

            # Check whether m and p are coprime
            if math.gcd(m, p) == 1:

                return eulerTotient(m) * eulerTotient(p)

    return None


n = int(input("Enter a number: "))

if n <= 0:
    print("Enter a positive integer.")

else:
    result = eulerTotient(n)
    print("Euler Totient Value:", result)


