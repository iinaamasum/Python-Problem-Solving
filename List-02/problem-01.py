""" Create a function exp(a, n) that returns the exponential result ( an ). Read user input a and n in a single line from the keyboard.

Example input:
>> enter numbers: 2 3

Example Output:
>> result is: 8 """


def exp(a, n):
    return a**n


a, n = map(int, input("Enter numbers: ").split())

result = exp(a, n)
print("The result is:", result)
