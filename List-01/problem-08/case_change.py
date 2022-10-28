s = "hI there, I aM masum."


def make_upper():
    answer = s.upper()
    return answer


def make_capital():
    answer = s.split(" ")
    result = list()
    for word in answer:
        result.append(word.capitalize())
    return " ".join(result)


def make_lower():
    answer = s.lower()
    return answer


if __name__ == "__main__":
    print(make_upper())
    print(make_capital())
    print(make_lower())
