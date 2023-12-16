import pandas as pd
import pdb

# Creation of Series
s = pd.Series([1,2,3,4,5])
# print(s)

s = pd.Series([6, 7, 8, 9]).tolist()
# print(s)
# print(type(s))

x1 = pd.Series([2, 4, 6, 8, 10])
x2 = pd.Series([1, 3, 6, 7, 10])

# Basic Mathematical Operations
add = (x1 + x2)
subtract = (x1 - x2)
multiply = (x1 * x2)
divide = (x1 / x2)

# Boolean Comparison of Series
lte_bool = (x1 <= x2)
gt_bool = x1 > x2

pdb.set_trace()