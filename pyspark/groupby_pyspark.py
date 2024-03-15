from pyspark.sql import SparkSession
from pyspark.sql.functions import pandas_udf, col, sum, avg
from pyspark.sql.types import FloatType
import pandas as pd

spark = SparkSession.builder.appName("groupby pyspark") \
.master("local[*]").getOrCreate()

data = [("1001", "Laptop", "Electronics", 1, 1000, "2023-01-01"),
        ("1002", "Mouse", "Electronics", 2, 50, "2023-01-02"),
        ("1003", "Laptop", "Electronics", 1, 1200, "2023-01-03"),
        ("1004", "Mouse", "Electronics", 3, 30, "2023-01-04"),
        ("1005", "Smartphone", "Electronics", 1, 700, "2023-01-05")
    ]

columns = ["OrderID", "Product", "Category", "Quantity", "Price", "Date"]

df = spark.createDataFrame(data, columns)

# GroupBy on one column
product_sale_df = df.groupBy("Product").agg(sum("price").alias("Total Sales"))
product_sale_df.show()

# GroupBy on multiple column
product_sale_df_1 = df.groupBy(["Product", "Category"]).agg(sum("Price").alias("Total Sales"))
product_sale_df_1.show() 

# GroupBy with multiple aggregation
product_sale_df_2 = df.groupBy("Product").agg(sum("Price").alias("Total Sales") , sum("Quantity").alias("Total Quantity"))
product_sale_df_2.show()

# GroupBy with filter using Where
product_sale_df_3 = df.groupBy("Product") \
    .agg(avg("Price").alias("Total Sales"), 
         sum("Quantity").alias("Total Quantity")) \
    .where(col("Total Quantity") >= 2)
product_sale_df_3.show()

# custom Aggregation

@pandas_udf(FloatType())
def median(column: pd.Series) -> float:
    return float(column.median())

result = df.groupBy("Category") \
    .agg(median("Price").alias("Median_Price"))

result.show()