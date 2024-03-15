from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder.appName("groupby and orderby pyspark") \
.master("local[*]").getOrCreate()

data = [
    ("Alice", 30, "New York"),
    ("Bob", 28, "San Francisco"),
    ("Charlie", 34, "Los Angeles"),
    ("Diana", 29, "Chicago")
]

columns = ["Name", "Age", "City"]
df = spark.createDataFrame(data, columns)

sorted_by_age = df.orderBy("Age")
# sort is alias of orderBy
# sorted_by_age = df.sort("Age") 
sorted_by_age.show()

sorted_df = df.orderBy([desc("Age"), "City"])
sorted_df.show()