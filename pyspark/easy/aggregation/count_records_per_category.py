"""
Problem: Count records per category

Description:
Count number of records for each category in a transactional DataFrame.

Expected Output:
Columns: category, count.

Pattern: Aggregation
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
        pass


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("count_records_per_category")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [('books',), ('books',), ('electronics',), ('grocery',), ('grocery',), ('grocery',)]
    columns = ['category']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
