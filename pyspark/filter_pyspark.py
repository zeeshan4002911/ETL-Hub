from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("Different ways of Filter in pyspark") \
.master("local[*]").getOrCreate()

data = [
    Row(id=1, name="Alice", age=30),
    Row(id=2, name="Bob", age=25),
    Row(id=3, name="Charlie", age=35),
    Row(id=4, name="David", age=28)
]

df = spark.createDataFrame(data)

# Filter method
df = df.filter(df.age > 29)
df.show()

# Filter using where method
df = df.where(col('name').isin(['Alice', 'Charlie']))
df.show()

# Filter usign SQL Query
df.createOrReplaceTempView("people")
df = spark.sql("Select * from people where age <= 30")
df.show()

# Combining Multiple Filter Condition 
df = spark.createDataFrame(data)
df = df.filter((df.age > 25) & (df.name != "David"))
df.show()