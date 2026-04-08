"""
Problem: Remove duplicates with window function

Description:
Keep latest event per id by ordering on update timestamp.

Expected Output:
Deduplicated output with latest rows.

Pattern: Data Cleaning
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
        df1 = df.withColumn('updated_at', to_timestamp('updated_at'))
        w = Window.partitionBy('id').orderBy(col('updated_at').desc())
        return df1.withColumn('rn', row_number().over(w)).filter(col('rn') == 1).drop('rn')


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("remove_duplicates_with_window_function")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [(1, 'v1', '2026-04-07 09:00:00'), (1, 'v2', '2026-04-07 10:00:00'), (2, 'x1', '2026-04-07 09:30:00')]
    columns = ['id', 'value', 'updated_at']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
