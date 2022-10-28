""" 
Write a python to read three floating numbers from the keyboard in a single line with ‘-’ (dash) in between and output their sum.

Example input:
>> enter numbers: 2.3-4.5-1.7

Example Output:
>> sum is: 8.5

"""


def dash_number_sum():
    s = input("Enter numbers: ")
    l = s.split("-")
    answer = 0.0
    for val in l:
        answer += float(val)
    print("Sum is:", answer)


dash_number_sum()
