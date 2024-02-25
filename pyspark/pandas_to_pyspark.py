import pandas as pd
from pyspark.sql import SparkSession

data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "city": "Los Angeles"}
]

df_pandas = pd.DataFrame(data)
print(type(df_pandas))
print(df_pandas.head())

spark = SparkSession.builder.appName("Pandas to PySpark Dataframe") \
.master("local[*]").getOrCreate()

# Pandas dataframe to pyspark
df_pyspark = spark.createDataFrame(df_pandas)
print(type(df_pyspark))
print(df_pyspark.head())

# Pyspark dataframe to pandas
df = df_pyspark.toPandas()
print(type(df))
print(df.head())

spark.stop()