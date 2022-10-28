""" 
Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
Input:
numbers= [10,20,10,40,50,60,70]
target=50 
Output: 3, 4

"""


class IndexSum:
    numbers = [10, 20, 10, 40, 50, 60, 70]
    print("Inputs are: ", numbers)

    target = 50
    print("Target: ", target)
    val = 50
    idx = []
    for i in range(len(numbers)):
        val = 50
        idx = []
        flag = False
        for j in range(i, len(numbers)):
            if val == 0:
                flag = True
                break
            if val >= numbers[j]:
                val -= numbers[j]
                idx.append(j + 1)
        if flag:
            break
    print("Output: ", end="")
    for i, val in enumerate(idx):
        print(val, end="")
        if i < len(idx) - 1:
            print(", ", end="")
    print()


i = IndexSum()
