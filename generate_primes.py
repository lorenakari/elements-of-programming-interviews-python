def generate_primes(n: int) -> list:
    """Return a list with all the primes up to the integer n."""
    primes = []

    if n < 2:
        return []

    # is_prime[p] represents tells wether p is a prime or not
    # initially, set everything to true except for 0 and 1
    is_prime = [False, False] + [True] * (n - 1)

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)

        # sieve the multiples of primes
        multiple = 2 * i
        while multiple <= n:
            is_prime[multiple] = False
            multiple += i

    return primes


if __name__ == "__main__":
    n = 23
    print(generate_primes(n))
