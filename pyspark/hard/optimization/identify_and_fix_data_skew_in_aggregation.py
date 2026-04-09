"""
Problem: Identify and fix data skew in aggregation

Description:
Use salting to distribute skewed key during aggregation and then recombine partial results.

Expected Output:
Balanced aggregation output for skewed keys.

Pattern: Optimization
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
        salted = df.withColumn('salt', when(col('group_key') == 'hot', (rand() * 10).cast('int')).otherwise(lit(0)))
        partial = salted.groupBy('group_key', 'salt').agg(sum('value').alias('partial_sum'))
        return partial.groupBy('group_key').agg(sum('partial_sum').alias('total_value'))


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("identify_and_fix_data_skew_in_aggregation")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [('hot', 1), ('hot', 2), ('hot', 3), ('cold1', 1), ('cold2', 1)]
    columns = ['group_key', 'value']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
