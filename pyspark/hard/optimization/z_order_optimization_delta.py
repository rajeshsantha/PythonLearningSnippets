"""
Problem: Z-order optimization Delta

Description:
Simulate locality optimization by repartitioning and sorting on frequently filtered columns.

Expected Output:
DataFrame physically organized for faster selective reads.

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
        # In Delta this is typically: OPTIMIZE ... ZORDER BY (country, event_date)
        return df.repartition('country').sortWithinPartitions('country', 'event_date')


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("z_order_optimization_delta")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [(1, 'IN', '2026-04-06', 200), (2, 'US', '2026-04-06', 300), (3, 'IN', '2026-04-07', 150)]
    columns = ['id', 'country', 'event_date', 'amount']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
