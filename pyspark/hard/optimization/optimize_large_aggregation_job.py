"""
Problem: Optimize large aggregation job

Description:
Reduce shuffle volume for large groupBy by pre-partitioning and selective projection.

Expected Output:
Aggregated metrics with improved execution characteristics.

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
        projected = df.select('region', 'product_id', 'units')
        prepared = projected.repartition(8, col('region'))
        return prepared.groupBy('region', 'product_id').agg(sum('units').alias('total_units'))


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("optimize_large_aggregation_job")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [('east', 'p1', 10), ('east', 'p2', 20), ('west', 'p1', 5), ('west', 'p1', 15), ('west', 'p2', 7)]
    columns = ['region', 'product_id', 'units']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
