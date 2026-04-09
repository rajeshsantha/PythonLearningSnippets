"""
Problem: Detect duplicate events in stream

Description:
Deduplicate event stream by event_id while keeping first seen event.

Expected Output:
Deduplicated event stream.

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
        w = Window.partitionBy('event_id').orderBy(col('event_time').asc())
        return df1.withColumn('rn', row_number().over(w)).filter(col('rn') == 1).drop('rn')


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("detect_duplicate_events_in_stream")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [('e1', 'u1', '2026-04-07 10:00:00'), ('e1', 'u1', '2026-04-07 10:00:02'), ('e2', 'u2', '2026-04-07 10:01:00')]
    columns = ['event_id', 'user_id', 'event_time']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
