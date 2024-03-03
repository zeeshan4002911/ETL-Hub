from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, when, lit, concat_ws
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName('WithColumn Operation') \
.getOrCreate()

data = [(1, "Alice", 25), (2, "Bob", 30), (3, "Charlie", 15)]
columns = ["id", "name", "age"]

df = spark.createDataFrame(data, columns)
df.show()

# Renaming using withColumn
df = df.withColumn('years', col('age'))
df = df.drop('age')
df.show()

# Applying function using withColumn and expr function
df = df.withColumn('months', expr('years * 12'))
df.show()

# Changing the datatype of column
df = df.withColumn('id', col('id').cast(StringType()))
df.show()

# Conditional column using when 
df = df.withColumn('Category', when(col('years') < 18, lit('minor')).otherwise(lit('Adult')))
df.show()

# Column operation using multiple columns
df = df.withColumn('candidate_id', concat_ws("_", col('name'), col('id')))
df.show()