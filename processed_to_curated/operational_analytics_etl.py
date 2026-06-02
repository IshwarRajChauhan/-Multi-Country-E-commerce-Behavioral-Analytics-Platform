from pyspark.sql import SparkSession
from pyspark.sql.functions import count

spark = SparkSession.builder.getOrCreate()

logs = spark.read.parquet(
    "s3://ecommerce-analytics-lake-ishwar/processed/logs/"
)

ops_df = logs.groupBy(
    "country",
    "event_type"
).agg(
    count("*").alias("event_count")
)

ops_df.write.mode(
    "overwrite"
).parquet(
    "s3://ecommerce-analytics-lake-ishwar/curated/operational_analytics/"
)