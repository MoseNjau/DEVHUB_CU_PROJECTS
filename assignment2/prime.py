def is_prime(n):
    if n <= 1:  # Prime numbers are greater than 1
        return False
    elif n == 2:  # 2 is a prime number
        return True
    elif n % 2 == 0:  # Even numbers (except 2) are not prime
        return False
    else:
        # Check odd numbers from 3 up to the square root of n
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

# Test the function
print("Is 17 prime?", is_prime(17))
print("Is 15 prime?", is_prime(15))
