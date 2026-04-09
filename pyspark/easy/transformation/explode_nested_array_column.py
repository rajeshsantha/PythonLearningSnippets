"""
Problem: Explode nested array column

Description:
Flatten array column into multiple rows for downstream processing.

Expected Output:
Expanded rows per array element.

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
        return df.select("id", explode("tags").alias("tag"))


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("explode_nested_array_column")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [(1, ['a', 'b']), (2, ['c'])]
    columns = ['id', 'tags']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
