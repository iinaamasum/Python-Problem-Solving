""" 
Write a class with two instance variables X, n . Add two methods sum() and pow() to get the sum of X+n and exponential/power of Xn .

"""


class SumPow:
    def __init__(self, X, n) -> None:
        self.X = X
        self.n = n

    def sum(self):
        return self.X + self.n

    def pow(self):
        return self.X**self.n


X = int(input("Enter X: "))
n = int(input("Enter n: "))
obj = SumPow(X, n)

sum_res = obj.sum()
pow_res = obj.pow()

print(f"Sum is: {sum_res} and Pow is: {pow_res}")
