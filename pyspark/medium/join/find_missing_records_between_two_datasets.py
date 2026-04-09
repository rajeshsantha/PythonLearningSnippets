"""
Problem: Find missing records between two datasets

Description:
Identify source records missing in target using anti join.

Expected Output:
Missing records DataFrame.

Pattern: Join
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
        spark = df.sparkSession
        target = spark.createDataFrame([(1, 'A'), (3, 'C')], ['id', 'value'])
        return df.join(target.select('id'), on='id', how='left_anti')


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("find_missing_records_between_two_datasets")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [(1, 'A'), (2, 'B'), (3, 'C')]
    columns = ['id', 'value']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
