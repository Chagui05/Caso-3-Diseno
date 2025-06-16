from pyspark.sql import SparkSession
import os


# Create a SparkSession
spark = SparkSession.builder \
    .appName("MongoToS3") \
    .config("spark.mongodb.read.connection.uri", os.getenv("MONGO_URI")) \
    .config("spark.mongodb.read.database", "test") \
    .config("spark.mongodb.read.collection", "releases") \
    .config("spark.hadoop.fs.s3a.aws.credentials.provider", "com.amazonaws.auth.DefaultAWSCredentialsProviderChain") \
    .getOrCreate()

# Define the S3 path (using s3a protocol)
s3_bucket_path_json = "s3a://diseno-bucket/bronze-data/json"
s3_bucket_path_parquet = "s3a://diseno-bucket/bronze-data/parquet"

dataFrame = spark.read.format("mongodb").load();

dataFrame.printSchema()


dataFrame.write.mode("overwrite").json(s3_bucket_path_json)
dataFrame.write.mode("overwrite").parquet(s3_bucket_path_parquet)
