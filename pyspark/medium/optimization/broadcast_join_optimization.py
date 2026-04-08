"""
Problem: Broadcast join optimization

Description:
Use broadcast hint when one side is small to avoid expensive shuffle.

Expected Output:
Joined DataFrame produced with broadcast strategy.

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
        spark = df.sparkSession
        products = spark.createDataFrame(
            [('p1', 'Keyboard'), ('p2', 'Mouse'), ('p3', 'Monitor')],
            ['product_id', 'product_name']
        )
        return df.join(broadcast(products), on='product_id', how='left')


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("broadcast_join_optimization")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [(1001, 'p1', 2), (1002, 'p2', 1), (1003, 'p3', 5)]
    columns = ['order_id', 'product_id', 'qty']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
