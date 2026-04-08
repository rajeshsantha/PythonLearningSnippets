"""
Problem: Read streaming data from Kafka

Description:
Parse Kafka-like JSON payloads into structured columns (batch simulation).

Expected Output:
Structured stream-like DataFrame with event_id and metric.

Pattern: Streaming
Difficulty: Medium
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
        schema = 'event_id STRING, metric INT'
        return df.select(from_json(col('value'), schema).alias('json')).select('json.*')


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("read_streaming_data_from_kafka")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [('k1', '{"event_id":"e1","metric":10}'), ('k2', '{"event_id":"e2","metric":20}')]
    columns = ['key', 'value']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
