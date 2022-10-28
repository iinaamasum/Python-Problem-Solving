""" 
Write a python program to reverse every word from a given string s and output a new string. The position of words will remain the same, but their contents will be in reverse order.

s = “Programming Hero is the best”

Expected output: “gnimmargorP oreH si eht tseb”

"""


def reverse_string():
    s = "Programming Hero is the best"
    l = s.split(" ")
    answer = ""
    for i, word in enumerate(l):
        answer += word[-1::-1]
        if i < len(l) - 1:
            answer += " "

    print(answer)


reverse_string()
