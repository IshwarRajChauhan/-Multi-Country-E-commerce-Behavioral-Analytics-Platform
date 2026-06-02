from pyspark.sql import SparkSession
from pyspark.sql.functions import countDistinct,count,sum

spark = SparkSession.builder.getOrCreate()

orders = spark.read.parquet(
    "s3://ecommerce-analytics-lake-ishwar/processed/orders/"
)

clickstream = spark.read.parquet(
    "s3://ecommerce-analytics-lake-ishwar/processed/clickstream/"
)

customer_df = clickstream.join(
    orders,
    on="user_id",
    how="left"
)

customer_analytics = customer_df.groupBy(
    "user_id"
).agg(
    countDistinct("page").alias("pages_visited"),
    count("order_id").alias("orders_placed"),
    sum("amount").alias("lifetime_value")
)

customer_analytics.write.mode(
    "overwrite"
).parquet(
    "s3://ecommerce-analytics-lake-ishwar/curated/customer_analytics/"
)