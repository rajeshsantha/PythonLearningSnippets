"""
Problem: Handle null-safe joins

Description:
Join datasets using null-safe equality to correctly match null keys.

Expected Output:
Accurate join results including null-key matches.

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
        customers = spark.createDataFrame([(1, 'Alice'), (None, 'Unknown'), (3, 'Charlie')], ['customer_id', 'customer_name'])
        return df.join(customers, df.customer_id.eqNullSafe(customers.customer_id), 'inner')


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("handle_null_safe_joins")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [(1, 'o1'), (None, 'o2'), (2, 'o3')]
    columns = ['customer_id', 'order_id']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
