replace_with = [
    "chief",
    "thief",
    "superintendent",
    "sweeper",
    "married",
    "left",
    "tried",
    "died",
]

s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."


def change_story():
    s_list = s.split(" ")
    answer = ""
    for word in s_list:
        flag = False
        for i, val in enumerate(replace_with):
            if val == word and i < len(replace_with) - 1:
                answer += replace_with[i + 1]
                replace_with.remove(replace_with[i])
                replace_with.remove(replace_with[i])
                flag = True
                break
        if flag == False:
            answer += word
        answer += " "
    print(answer)


change_story()
