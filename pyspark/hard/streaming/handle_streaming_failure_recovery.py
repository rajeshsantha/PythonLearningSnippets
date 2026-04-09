"""
Problem: Handle streaming failure recovery

Description:
Demonstrate idempotent processing behavior used with checkpoint-based recovery.

Expected Output:
No duplicate output after simulated restart.

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
        # In production this would be paired with writeStream + checkpoint.
        # Idempotency here is simulated by removing duplicates by event_id.
        return df.dropDuplicates(['event_id'])


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("handle_streaming_failure_recovery")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [('b1', 'e1', 10), ('b1', 'e2', 15), ('b1', 'e2', 15), ('b2', 'e3', 20)]
    columns = ['batch_id', 'event_id', 'metric']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
