"""
Problem: Unpivot columns to rows

Description:
Convert metric columns into key-value rows for normalized analytics model.

Expected Output:
Normalized DataFrame with metric_name and metric_value.

Pattern: Transformation
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
        return df.select(
            'id',
            expr("stack(2, 'clicks', clicks, 'views', views) as (metric_name, metric_value)")
        )


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("unpivot_columns_to_rows")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [(1, 10, 20), (2, 30, 40)]
    columns = ['id', 'clicks', 'views']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
