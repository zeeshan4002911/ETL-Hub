from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType

data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "San Francisco"},
    {"name": "Charlie", "age": 55, "city": "Los Angeles"}
]

spark = SparkSession.builder.appName("UDF Example") \
.master("local[*]").getOrCreate()

df = spark.createDataFrame(data)

def age_group_cal(age):
    if age < 30:
        return 'Young'
    elif age < 45:
        return 'Middle-aged'
    else :
        return 'Old'
    
age_group_udf = udf(age_group_cal, StringType())

df = df.withColumn("age_group", age_group_udf(col('age')))
df.show(5, 0)

spark.stop()