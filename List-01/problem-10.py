a = ["oh", "Emelia", "to"]

s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."


def create_new_string():
    remove_comma = s.replace(",", "")
    s_list = remove_comma.split(" ")
    answer = ""
    for i, word in enumerate(s_list):
        flag = False
        for val in a:
            if word.lower() == val.lower():
                answer += s_list[i + 1]
                flag = True
                break
        if flag:
            answer += " "

    """ answer in sample output is wrong as "I and Emelia love to visit" line also contains 'to' thats means the answer would be "I love visit Bangladesh." """

    with open("out.txt", "w") as output:
        output.write(answer)
        output.close()
    print(answer)


create_new_string()
