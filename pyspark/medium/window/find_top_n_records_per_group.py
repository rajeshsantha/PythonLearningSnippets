"""
Problem: Find top N records per group

Description:
Get top 3 employees by salary for each department using window ranking.

Expected Output:
dept, employee, salary for top-ranked rows.

Pattern: Window
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
        w = Window.partitionBy("dept").orderBy(col("salary").desc())
        return (
            df.withColumn("rank", row_number().over(w))
            .filter(col("rank") <= 3)
            .drop("rank")
        )


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("find_top_n_records_per_group")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [('eng', 'e1', 120000), ('eng', 'e2', 140000), ('eng', 'e3', 130000), ('eng', 'e4', 110000), ('sales', 's1', 90000), ('sales', 's2', 85000), ('sales', 's3', 95000)]
    columns = ['dept', 'employee', 'salary']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
