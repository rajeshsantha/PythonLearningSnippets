"""
Problem: Late arriving data handling

Description:
Handle late events by discarding records beyond allowed lateness and aggregating remaining data.

Expected Output:
Correct aggregates after lateness handling.

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
        max_ts = df1.agg(max('event_time').alias('m')).collect()[0]['m']
        # Simulate watermark of 30 minutes in batch mode.
        recent = df1.filter(col('event_time') >= lit(max_ts) - expr('INTERVAL 30 MINUTES'))
        return recent.groupBy('user_id').agg(sum('clicks').alias('total_clicks'))


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("late_arriving_data_handling")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [('u1', '2026-04-07 10:00:00', 1), ('u1', '2026-04-07 10:04:00', 1), ('u1', '2026-04-07 09:20:00', 1), ('u2', '2026-04-07 10:01:00', 1)]
    columns = ['user_id', 'event_time', 'clicks']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
