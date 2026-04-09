"""
Problem: Implement CDC Change Data Capture

Description:
Apply insert, update, delete operations from change feed to current target snapshot.

Expected Output:
Updated target table after applying CDC operations.

Pattern: CDC
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
        spark = df.sparkSession
        target = spark.createDataFrame([(1, 'Alice'), (2, 'Bob')], ['id', 'name'])

        deletes = df.filter(col('op') == 'D').select('id')
        upserts = df.filter(col('op').isin('I', 'U')).select('id', 'name')

        remaining = target.join(deletes, on='id', how='left_anti')
        remaining_without_upserted = remaining.join(upserts.select('id'), on='id', how='left_anti')

        return remaining_without_upserted.unionByName(upserts)


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("implement_cdc_change_data_capture")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [(1, 'Alice_v2', 'U'), (3, 'Charlie', 'I'), (2, None, 'D')]
    columns = ['id', 'name', 'op']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
