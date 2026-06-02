from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.json(
    "s3://ecommerce-analytics-lake-ishwar/raw/*/clickstream/"
)

valid_df = df.filter(
    (df.user_id.isNotNull()) &
    (df.country.isNotNull()) &
    (df.page.isNotNull())
)

invalid_df = df.subtract(valid_df)

valid_df.write.mode(
    "overwrite"
).partitionBy(
    "country"
).parquet(
    "s3://ecommerce-analytics-lake-ishwar/processed/clickstream/"
)

invalid_df.write.mode(
    "overwrite"
).parquet(
    "s3://ecommerce-analytics-lake-ishwar/invalid/clickstream/"
)