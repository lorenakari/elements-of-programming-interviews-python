def reverse_bits(x: int) -> int:
    """Return the 64-bit unsigned integer consisting of the input in reverse
    order (in binary)"""
    for i in range(32):
        # Check if the bits are different and if they are, flip them
        if (x >> i) & 1 != (x >> (64 - i)) & 1:
            # Select the bits to flip with a bit mask
            mask = (1 << i) | (1 << (64 - i))
            # Flip the bits with xor and the mask (1 xor 1 = 0, and 1 xor 0 = 1)
            x ^= mask
    return x


if __name__ == "__main__":
    n = 1000
    print(n)
    print(bin(n))
    reversed = reverse_bits(n)
    print(bin(reversed))
    print(reversed)
