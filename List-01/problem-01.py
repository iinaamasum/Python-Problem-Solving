l = ["This", "is", "very", "fantastic"]


def create_string():
    answer = '"'
    for i, word in enumerate(l):
        answer += word
        if i != len(l) - 1:
            answer += " "
    answer += '"'
    print(answer)


create_string()
