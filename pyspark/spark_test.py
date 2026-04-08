from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").appName("test").getOrCreate()
print("Spark session created:", spark)
print("Spark version:", spark.version)
spark.stop()
