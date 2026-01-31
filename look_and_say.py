def look_and_say(s: str) -> str:
    result = []
    i = 0
    while i < len(s):
        digit = s[i]
        count = 1
        while (i + count < len(s)) and (s[i + count] == digit):
            count += 1
        i += count
        result.append(str(count) + digit)
    return "".join(result)


def look_and_say_up_to_n(n: int) -> str:
    look_and_say_string = str(n)
    for i in range(n):
        look_and_say_string = look_and_say(look_and_say_string)
    return look_and_say_string


if __name__ == "__main__":
    n = 11
    print(f"Result: {look_and_say_up_to_n(n)}")
