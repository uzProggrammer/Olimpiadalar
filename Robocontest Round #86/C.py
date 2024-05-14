def is_almost_prime(n):
    """
    Checks if a number is almost prime (has exactly 2 divisors).

    Args:
        n: The number to check.

    Returns:
        True if the number is almost prime, False otherwise.
    """
    if n <= 1:
        return False
    divisor_count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisor_count += 1
            if divisor_count > 3:
                return False
    return divisor_count == 3

def count_almost_primes(l, r):
    """
    Counts the number of almost prime numbers in a range (inclusive).

    Args:
        l: The lower bound of the range.
        r: The upper bound of the range.

    Returns:
        The number of almost prime numbers in the range.
    """
    count = 0
    for num in range(l, r + 1):
        if is_almost_prime(num):
            count += 1
    return count

# Get number of queries
t = int(input())

# Process each query
for _ in range(t):
    # Get range bounds
    l, r = map(int, input().split())

    # Count and print almost prime numbers in the range
    almost_prime_count = count_almost_primes(l, r)
    print(almost_prime_count)
