"""
Problem: Handle out of order data in stream

Description:
Process out-of-order events and compute minute-level aggregates by event time.

Expected Output:
Correct event-time aggregates.

Pattern: Streaming
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
        df1 = df.withColumn('event_time', to_timestamp('event_time'))
        return (
            df1.groupBy(window(col('event_time'), '1 minute').alias('win'))
            .agg(sum('value').alias('total_value'))
            .orderBy(col('win.start'))
        )


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("handle_out_of_order_data_in_stream")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [('2026-04-07 10:02:00', 5), ('2026-04-07 10:00:00', 3), ('2026-04-07 10:01:00', 4)]
    columns = ['event_time', 'value']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
