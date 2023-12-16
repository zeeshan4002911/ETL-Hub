import pandas as pd

s = pd.Series([1,2,3,4,5])
# print(s)

s = pd.Series([6, 7, 8, 9]).tolist()
# print(s)
# print(type(s))

x1 = pd.Series([2, 4, 6, 8, 10])
x2 = pd.Series([1, 3, 5, 7, 10])

# print(x1 + x2)
# print(x1 - x2)
# print(x1 * x2)
# print(x1 / x2)