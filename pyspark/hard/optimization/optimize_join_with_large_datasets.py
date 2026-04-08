"""
Problem: Optimize join with large datasets

Description:
Optimize large-large join by repartitioning both sides on join key.

Expected Output:
Joined DataFrame with reduced shuffle skew.

Pattern: Optimization
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
        customers = spark.createDataFrame([(1, 'A'), (2, 'B'), (3, 'C')], ['customer_id', 'name'])
        left = df.repartition(8, col('customer_id'))
        right = customers.repartition(8, col('customer_id'))
        return left.join(right, on='customer_id', how='left')


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("optimize_join_with_large_datasets")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [(1, 'o1'), (2, 'o2'), (3, 'o3'), (4, 'o4')]
    columns = ['customer_id', 'order_id']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
