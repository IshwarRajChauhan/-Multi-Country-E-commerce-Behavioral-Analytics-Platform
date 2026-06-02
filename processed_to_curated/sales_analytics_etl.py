from pyspark.sql import SparkSession
from pyspark.sql.functions import count,sum,avg

spark = SparkSession.builder.getOrCreate()

orders = spark.read.parquet(
    "s3://ecommerce-analytics-lake-ishwar/processed/orders/"
)

sales_df = orders.groupBy(
    "country"
).agg(
    count("order_id").alias("total_orders"),
    sum("amount").alias("total_revenue"),
    avg("amount").alias("avg_order_value")
)

sales_df.write.mode(
    "overwrite"
).parquet(
    "s3://ecommerce-analytics-lake-ishwar/curated/sales_analytics/"
)