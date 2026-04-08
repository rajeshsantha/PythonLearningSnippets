"""
Problem: Running total using window

Description:
Calculate cumulative sales by region ordered by date.

Expected Output:
region, date, sales, running_total.

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
        df1 = df.withColumn("date", to_date("date"))
        w = Window.partitionBy("region").orderBy("date").rowsBetween(Window.unboundedPreceding, Window.currentRow)
        return df1.withColumn("running_total", sum("sales").over(w))


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("running_total_using_window")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [('east', '2026-04-01', 100), ('east', '2026-04-02', 150), ('west', '2026-04-01', 80), ('west', '2026-04-03', 120)]
    columns = ['region', 'date', 'sales']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
