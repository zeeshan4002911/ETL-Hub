from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import *

spark = SparkSession.builder.appName('Different ways to Rename Column') \
.master('local[*]').getOrCreate()

data = [Row(name="Alice", age=25, city="New York"),
        Row(name="Bob", age=30, city="San Francisco"),
        Row(name="Cathy", age=35, city="Los Angeles")]

df = spark.createDataFrame(data)
df.show()

# Rename using inbuilt withColumnRename method
df = df.withColumnRenamed('age', 'user_age')
df.show()

# Rename using alias and select
df = df.select('name', 'city', col('user_age').alias('age'))
df.show()

# Rename using toDF method
df = df.toDF('user_name', 'user_city', 'user_age')
df.show()

# Multiple column rename
df = df.withColumnRenamed("user_name", "name") \
        .withColumnRenamed("user_age", "age") \
        .withColumnRenamed("user_city", "city")
df.show()