"""
Problem: Filter null or invalid records

Description:
Remove rows where id is null or name is null/blank before downstream joins.

Expected Output:
Cleaned DataFrame with valid id and name.

Pattern: Data Cleaning
Difficulty: Easy
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
        return df.filter(
            col("id").isNotNull() & col("name").isNotNull() & (trim(col("name")) != "")
        )


if __name__ == "__main__":
    import os, sys

    # Ensure SPARK_HOME and JAVA_HOME are set (critical for PyCharm)
    os.environ.setdefault("SPARK_HOME", "/Users/rajeshsantha/spark411")
    os.environ.setdefault("JAVA_HOME", "/opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home")

    # Optional: use findspark to auto-locate and initialize Spark
    try:
        import findspark
        findspark.init(os.environ["SPARK_HOME"])
    except Exception:
        pass

    spark = SparkSession.builder \
        .appName("filter_null_or_invalid_records") \
        .master("local[*]") \
        .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [(1, 'Alice'), (2, ''), (None, 'Bob'), (3, 'Charlie'), (4, None)]
    columns = ['id', 'name']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
