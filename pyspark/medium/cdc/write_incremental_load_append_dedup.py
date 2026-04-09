"""
Problem: Write incremental load append dedup

Description:
Append daily records and deduplicate by business key + event timestamp.

Expected Output:
Unified incremental dataset without duplicates.

Pattern: CDC
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
        spark = df.sparkSession
        historical = spark.createDataFrame(
            [('2026-04-05', 1, 'A_old', '2026-04-05 08:00:00')],
            ['batch_date', 'id', 'status', 'event_ts']
        )
        combined = historical.unionByName(df).withColumn("event_ts", to_timestamp("event_ts"))
        w = Window.partitionBy("id").orderBy(col("event_ts").desc())
        return combined.withColumn("rn", row_number().over(w)).filter(col("rn") == 1).drop("rn")


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("write_incremental_load_append_dedup")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [('2026-04-06', 1, 'A', '2026-04-06 10:00:00'), ('2026-04-07', 1, 'A_new', '2026-04-07 09:00:00'), ('2026-04-07', 2, 'B', '2026-04-07 11:00:00')]
    columns = ['batch_date', 'id', 'status', 'event_ts']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
