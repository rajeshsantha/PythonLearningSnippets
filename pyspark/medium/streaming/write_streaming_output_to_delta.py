"""
Problem: Write streaming output to Delta

Description:
Prepare streaming output with checkpoint-compatible idempotent records (Delta write simulated).

Expected Output:
Durable output dataset ready for sink write.

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
        # In production: writeStream.format('delta').option('checkpointLocation', ...)
        return df.dropDuplicates(['event_id']).withColumn('processed_at', current_timestamp())


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("write_streaming_output_to_delta")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [('e1', 10), ('e2', 20), ('e2', 20)]
    columns = ['event_id', 'metric']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
