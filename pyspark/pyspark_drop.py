from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import re

spark = SparkSession.builder.appName("Drop Example") \
.getOrCreate()

data = [("Alice", 30, "New York", "F"),
        ("Bob", 28, "San Francisco", "M"),
        ("Cathy", 29, "Los Angeles", "F"),
        ("David", 32, "Chicago", "M")]
columns = ['name', 'age', 'city', 'gender']

df = spark.createDataFrame(data, columns)
df.show()

# Drop single column
df = df.drop('gender')
df.show()

# Drop multiple columns
dropCol = ['city', 'age', 'name']
df = df.drop(*dropCol)
df.show()

df = spark.createDataFrame(data, columns)

# Conditional column drop
if 'gender' in df.columns:
    df = df.drop('gender')
    df.show()

# Drop using pattern
pattern = 'age|city'
df = df.select([col(c) for c in df.columns if not re.match(pattern, c)])
df.show()
    
