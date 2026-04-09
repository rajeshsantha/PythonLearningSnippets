"""
Problem: Sliding window aggregation

Description:
Compute average clicks over 10-minute window with 5-minute slide.

Expected Output:
time_window, avg_clicks.

Pattern: Streaming
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
        df1 = df.withColumn('event_time', to_timestamp('event_time'))
        return (
            df1.groupBy(window(col('event_time'), '10 minutes', '5 minutes').alias('time_window'))
            .agg(avg('clicks').alias('avg_clicks'))
            .orderBy(col('time_window.start'))
        )


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("sliding_window_aggregation")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [('2026-04-07 10:00:00', 5), ('2026-04-07 10:03:00', 8), ('2026-04-07 10:07:00', 4), ('2026-04-07 10:11:00', 10)]
    columns = ['event_time', 'clicks']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
