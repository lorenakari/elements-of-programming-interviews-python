def is_well_formed(s: str) -> bool:
    left_chars = []
    lookup = {"{": "}", "[": "]", "(": ")"}

    for c in s:
        if c in lookup:
            left_chars.append(c)
        elif not left_chars or lookup[left_chars.pop()] != c:
            return False

    return not left_chars


valid = "{([])}"
not_valid = "{[(]}"
print(is_well_formed(valid))
print(is_well_formed(not_valid))
