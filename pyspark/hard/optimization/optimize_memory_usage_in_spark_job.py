"""
Problem: Optimize memory usage in Spark job

Description:
Reduce memory pressure by selecting required columns, downcasting, and partition-aware aggregation.

Expected Output:
Stable aggregation with lower memory footprint.

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
        projected = df.select('category', col('amount').cast('float'))
        prepared = projected.repartition(4, col('category')).persist()
        return prepared.groupBy('category').agg(sum('amount').alias('total_amount'))


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("optimize_memory_usage_in_spark_job")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [('u1', 'cat1', 10.0, 'unused_a'), ('u2', 'cat1', 20.0, 'unused_b'), ('u3', 'cat2', 15.0, 'unused_c')]
    columns = ['user_id', 'category', 'amount', 'debug_payload']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
