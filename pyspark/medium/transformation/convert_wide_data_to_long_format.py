"""
Problem: Convert wide data to long format

Description:
Normalize wide KPI columns into long key-value format.

Expected Output:
Long-format DataFrame.

Pattern: Transformation
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
        return df.select(
            'store_id',
            expr("stack(3, 'sales', sales, 'returns', returns, 'visits', visits) as (metric, value)")
        )


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("convert_wide_data_to_long_format")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [('store_1', 100, 70, 50), ('store_2', 120, 80, 60)]
    columns = ['store_id', 'sales', 'returns', 'visits']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
