"""
Problem: Partition data while writing

Description:
Prepare data partitioned by event_date for efficient pruning.

Expected Output:
DataFrame partitioned by date key.

Pattern: Partitioning
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
        return df.repartition(col("event_date"))


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("partition_data_while_writing")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [('2026-04-06', 1, 10.0), ('2026-04-06', 2, 5.0), ('2026-04-07', 1, 20.0)]
    columns = ['event_date', 'id', 'amount']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
