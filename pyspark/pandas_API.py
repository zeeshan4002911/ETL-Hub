import pyspark.pandas as ps
import pandas as pd
import numpy as np

# Using pandas on pyspark api for creating series and dataframe
s = ps.Series([1, 3, 5, np.nan, 6, 8])

psdf = ps.DataFrame(
    {'a': [1, 2, 3, 4, 5, 6],
     'b': [100, 200, 300, 400, 500, 600],
     'c': ["one", "two", "three", "four", "five", "six"]},
    index=[10, 20, 30, 40, 50, 60])

dates = pd.date_range('20130101', periods=6)

# Pandas dataframe
pdf = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(type(pdf))
print(pdf.head())

# PySpark dataframe using from_pandas
psdf = ps.from_pandas(pdf)
print(type(psdf))
print(psdf.head())

# Pandas dataframe using to_pandas
pdf = psdf.to_pandas()
print(type(pdf))
print(pdf.head())

