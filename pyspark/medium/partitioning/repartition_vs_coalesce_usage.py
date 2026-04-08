"""
Problem: Repartition vs Coalesce usage

Description:
Increase partitions for parallelism and then coalesce for efficient writes.

Expected Output:
DataFrame with controlled partition count.

Pattern: Partitioning
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
        repartitioned = df.repartition(10, col("id"))
        return repartitioned.coalesce(5)


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("repartition_vs_coalesce_usage")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [(1, 'v1'), (2, 'v2'), (3, 'v3'), (4, 'v4'), (5, 'v5'), (6, 'v6'), (7, 'v7'), (8, 'v8'), (9, 'v9'), (10, 'v10'), (11, 'v11'), (12, 'v12'), (13, 'v13'), (14, 'v14'), (15, 'v15'), (16, 'v16'), (17, 'v17'), (18, 'v18'), (19, 'v19'), (20, 'v20')]
    columns = ['id', 'value']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
