"""
Problem: Compute sessionization from logs

Description:
Create user sessions using inactivity gap of 30 minutes.

Expected Output:
Rows with user_id, session_id, event_time.

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
        w = Window.partitionBy('user_id').orderBy('event_time')
        with_prev = df1.withColumn('prev_time', lag('event_time').over(w))
        with_flag = with_prev.withColumn(
            'new_session',
            when(col('prev_time').isNull(), 1)
            .when((col('event_time').cast('long') - col('prev_time').cast('long')) > 30 * 60, 1)
            .otherwise(0)
        )
        return with_flag.withColumn('session_id', sum('new_session').over(w)).drop('prev_time', 'new_session')


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("compute_sessionization_from_logs")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [('u1', '2026-04-07 10:00:00'), ('u1', '2026-04-07 10:10:00'), ('u1', '2026-04-07 10:50:00'), ('u2', '2026-04-07 09:00:00'), ('u2', '2026-04-07 09:20:00')]
    columns = ['user_id', 'event_time']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
