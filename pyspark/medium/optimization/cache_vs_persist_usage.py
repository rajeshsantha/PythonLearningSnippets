"""
Problem: Cache vs persist usage

Description:
Persist reused DataFrame to avoid recomputation in multi-step pipelines.

Expected Output:
Reused DataFrame with stable performance.

Pattern: Optimization
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
        cached = df.filter(col('metric') > 0).persist()
        summary = cached.groupBy('group_id').agg(avg('metric').alias('avg_metric'))
        return summary.orderBy('group_id')


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("cache_vs_persist_usage")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [('A', 10), ('A', 20), ('B', 5), ('B', 7)]
    columns = ['group_id', 'metric']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
