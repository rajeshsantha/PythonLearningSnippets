"""
Problem: Join two DataFrames inner join

Description:
Join orders with customer master on customer_id to enrich transactions.

Expected Output:
Joined DataFrame with order and customer attributes.

Pattern: Join
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
        spark = df.sparkSession
        customers = spark.createDataFrame(
            [(1, "Alice"), (2, "Bob"), (3, "Charlie")],
            ["customer_id", "customer_name"],
        )
        return df.join(customers, on="customer_id", how="inner")


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("join_two_dataframes_inner_join")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [(101, 1, 250.0), (102, 2, 120.0), (103, 4, 99.0)]
    columns = ['order_id', 'customer_id', 'amount']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
