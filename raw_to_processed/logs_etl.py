from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.option(
    "header",
    "true"
).csv(
    "s3://ecommerce-analytics-lake-ishwar/raw/*/logs/"
)

valid_df = df.filter(
    (df.log_id.isNotNull()) &
    (df.event_type.isNotNull()) &
    (df.country.isNotNull())
)

invalid_df = df.subtract(valid_df)

valid_df.write.mode(
    "overwrite"
).partitionBy(
    "country"
).parquet(
    "s3://ecommerce-analytics-lake-ishwar/processed/logs/"
)

invalid_df.write.mode(
    "overwrite"
).parquet(
    "s3://ecommerce-analytics-lake-ishwar/invalid/logs/"
)