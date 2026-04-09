"""
Problem: Perform multi column sorting

Description:
Sort records by date descending and id ascending.

Expected Output:
Sorted DataFrame.

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
        return df.orderBy(col("date").desc(), col("id").asc())


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("perform_multi_column_sorting")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [('2026-04-07', 2, 100), ('2026-04-07', 1, 80), ('2026-04-06', 3, 70)]
    columns = ['date', 'id', 'amount']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
