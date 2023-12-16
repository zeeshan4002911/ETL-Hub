from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('main').getOrCreate()
df = spark.read.csv('data.csv')
df = spark.read.option('header', 'true').csv('data.csv')

import pdb; pdb.set_trace()