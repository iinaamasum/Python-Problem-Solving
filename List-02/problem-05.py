""" 
Write a python program to read student_name and mark from keyboard and store the data in a text file with an unique student_id .

"""


import random


def student_info():
    info_lst = []
    student_name = input("Enter Student Name: ")
    mark = input("Enter Mark: ")
    student_id = str(random.randint(1, 100000)) + student_name.upper() + str(mark)
    info_lst.append(
        {"student_name": student_name, "mark": mark, "student_id": student_id}
    )
    with open("list.txt", "w") as output:
        output.write(str(info_lst))
    output.close()
    print("Info: ", info_lst)


student_info()
