"""
Problem: Remove duplicate records using primary key

Description:
Given records with duplicate id values, keep only the latest record per id using event timestamp.

Expected Output:
DataFrame with one latest row per id.

Pattern: Data Cleaning
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
        df1 = df.withColumn("event_ts", to_timestamp("event_ts"))
        w = Window.partitionBy("id").orderBy(col("event_ts").desc())
        return (
            df1.withColumn("rn", row_number().over(w))
            .filter(col("rn") == 1)
            .drop("rn")
        )


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("remove_duplicate_records_using_primary_key")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [(1, 'A', '2026-04-01 10:00:00'), (1, 'A_v2', '2026-04-01 11:00:00'), (2, 'B', '2026-04-01 09:30:00')]
    columns = ['id', 'name', 'event_ts']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
