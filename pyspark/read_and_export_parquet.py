from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Read And Export Parquet") \
    .master("local[*]").getOrCreate()

df = spark.read.csv('data-files/data.csv', header=True, inferSchema=True)
df.write.parquet("data-files/parquet-file")

spark.stop()