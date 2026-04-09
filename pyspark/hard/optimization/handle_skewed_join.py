"""
Problem: Handle skewed join

Description:
Mitigate skew where one join key dominates by using salting before join.

Expected Output:
Joined DataFrame with reduced skew impact.

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
        spark = df.sparkSession
        dim = spark.createDataFrame([('unknown', 'fallback'), ('k1', 'A'), ('k2', 'B')], ['join_key', 'label'])

        salted_fact = df.withColumn(
            "salt",
            when(col("join_key") == "unknown", (rand() * 10).cast("int")).otherwise(lit(0))
        )

        salts = spark.range(0, 10).withColumnRenamed("id", "salt")
        salted_dim = (
            dim.filter(col("join_key") == "unknown").crossJoin(salts)
            .unionByName(dim.filter(col("join_key") != "unknown").withColumn("salt", lit(0)))
        )
        return salted_fact.join(salted_dim, on=["join_key", "salt"], how="left").drop("salt")


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("handle_skewed_join")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [('unknown', 1), ('unknown', 2), ('unknown', 3), ('k1', 4), ('k2', 5)]
    columns = ['join_key', 'metric']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
