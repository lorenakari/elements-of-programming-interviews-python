def remove_dups(A: list) -> list:
    """Update the input sorted array so that repeated elements are removed and
    the remaining elements are shifted left to fill emptied indices and return
    the number of valid elements."""
    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index


if __name__ == "__main__":
    A = [1, 1, 1, 2, 3, 3, 4, 5, 6, 6, 6, 7, 7]
    print(A[: remove_dups(A)])
