""" 
Write a python program for the requirement below. Notice the output must be in sorted order -
Input  : x3b4U5i2
Output : bbbbiiUUUUUxxx

"""


def create_str():
    s = input("Input: ")
    answer = ""
    i = 1
    for j in range(0, len(s), 2):
        answer += s[j] * int(s[i])
        if i + 2 < len(s):
            i += 2
    res = "".join(sorted(answer, key=lambda s: s.lower()))
    print("Output:", res)


create_str()
