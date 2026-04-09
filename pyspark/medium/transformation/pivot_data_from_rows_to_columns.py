"""
Problem: Pivot data from rows to columns

Description:
Pivot transaction_type values into columns with aggregated amount.

Expected Output:
Pivoted DataFrame with one row per customer.

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
        return (
            df.groupBy('customer_id')
            .pivot('txn_type')
            .agg(sum('amount'))
            .na.fill(0)
        )


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("pivot_data_from_rows_to_columns")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [(1, 'debit', 100.0), (1, 'credit', 40.0), (2, 'debit', 70.0)]
    columns = ['customer_id', 'txn_type', 'amount']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
