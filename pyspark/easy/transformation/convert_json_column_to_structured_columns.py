"""
Problem: Convert JSON column to structured columns

Description:
Parse a JSON payload column into typed columns for analytics.

Expected Output:
Flattened DataFrame with id, city, score columns.

Pattern: Transformation
Difficulty: Easy
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window


class Solution:

    def solve(self, df):
        """
        Approach:
        - Apply PySpark DataFrame transformations to solve the problem.
        - Keep logic idempotent and production-oriented for data pipelines.

        Time Complexity:
        - Depends on data size and shuffle stages (typically O(n) to O(n log n)).

        Space Complexity:
        - Depends on partitioning, caching, and intermediate shuffles.
        """
        schema = "city STRING, score INT"
        parsed = df.withColumn("payload", from_json(col("payload_json"), schema))
        return parsed.select("id", col("payload.city").alias("city"), col("payload.score").alias("score"))


if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("convert_json_column_to_structured_columns") \
        .master("local[*]") \
        .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [('1', '{"city":"Bengaluru","score":91}'), ('2', '{"city":"Mumbai","score":87}')]
    columns = ['id', 'payload_json']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
