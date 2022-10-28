""" 
Write a Python class to get all possible unique subsets from a set of integers.
Input  : [4, 5, 6] 
Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

"""


class Subsets:
    def __init__(self) -> None:
        lst = list(map(int, input("Enter space separated numbers: ").strip().split()))

        result = []
        for i in range(2 ** len(lst)):
            temp = []
            for j in range(len(lst)):
                if i & (1 << j):
                    temp.append(lst[j])
            result.append(temp)

        print(result)


a = Subsets()
