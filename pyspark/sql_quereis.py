from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SQL Queries Execution") \
    .master("local[*]").getOrCreate()

df = spark.read.csv('data-files/data.csv', header=True, inferSchema=True)
df1 = df.createOrReplaceTempView("Salary")
result = spark.sql('SELECT * FROM Salary')
result.show()
spark.stop()