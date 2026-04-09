"""
Problem: Handle schema evolution in Delta

Description:
Merge incoming data with new columns into existing schema by adding missing columns.

Expected Output:
Unified dataset with evolved schema.

Pattern: Schema Evolution
Difficulty: Hard
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
        spark = df.sparkSession
        existing = spark.createDataFrame([(1, 'Alice')], ['id', 'name'])
        for c in set(df.columns) - set(existing.columns):
            existing = existing.withColumn(c, lit(None).cast(df.schema[c].dataType))
        for c in set(existing.columns) - set(df.columns):
            df = df.withColumn(c, lit(None).cast(existing.schema[c].dataType))
        return existing.select(sorted(existing.columns)).unionByName(df.select(sorted(df.columns)))


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("handle_schema_evolution_in_delta")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [(1, 'Alice', 'gold'), (2, 'Bob', 'silver')]
    columns = ['id', 'name', 'tier']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
