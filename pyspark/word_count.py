from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode, col

spark = SparkSession.builder.appName("Word Count") \
.master("local[*]").getOrCreate()

data = spark.read.text("data-files/input.txt")

words = data.select(explode(split(col("value"), " ")).alias("word"))

word_count = words.groupby("word").count()

word_count.show()

spark.stop()

