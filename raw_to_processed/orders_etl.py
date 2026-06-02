from pyspark.sql import SparkSession
from pyspark.sql.functions import current_date

spark = SparkSession.builder.getOrCreate()

df = spark.read.option(
    "header",
    "true"
).csv(
    "s3://ecommerce-analytics-lake-ishwar/raw/*/orders/"
)

df = df.dropDuplicates()

valid_df = df.filter(
    (df.amount > 0) &
    (df.user_id.isNotNull()) &
    (df.country.isNotNull())
)

invalid_df = df.subtract(valid_df)

valid_df = valid_df.withColumn(
    "ingestion_date",
    current_date()
)

valid_df.write.mode(
    "overwrite"
).partitionBy(
    "country"
).parquet(
    "s3://ecommerce-analytics-lake-ishwar/processed/orders/"
)

invalid_df.write.mode(
    "overwrite"
).parquet(
    "s3://ecommerce-analytics-lake-ishwar/invalid/orders/"
)