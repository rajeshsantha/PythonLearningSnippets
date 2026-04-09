"""
Problem: Implement slowly changing dimension SCD Type 2

Description:
Maintain historical customer attributes by closing old records and inserting new active versions.

Expected Output:
SCD2 table with effective_start, effective_end, is_current.

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
        current = spark.createDataFrame(
            [(1, 'Alice', 'standard', '2026-01-01', None, True), (2, 'Bob', 'basic', '2026-01-01', None, True)],
            ['id', 'name', 'segment', 'effective_start', 'effective_end', 'is_current']
        )

        changed = current.alias('t').join(df.alias('s'), on='id', how='inner').filter(col('t.segment') != col('s.segment'))
        closed = changed.select(
            col('t.id'), col('t.name'), col('t.segment'), col('t.effective_start'),
            date_sub(to_date(col('s.as_of_date')), 1).cast('string').alias('effective_end'),
            lit(False).alias('is_current')
        )
        unchanged = current.join(changed.select(col('t.id').alias('id_changed')), current.id == col('id_changed'), 'left_anti')
        new_versions = changed.select(
            col('s.id'), col('s.name'), col('s.segment'), col('s.as_of_date').alias('effective_start'),
            lit(None).cast('string').alias('effective_end'), lit(True).alias('is_current')
        )
        inserts = df.join(current.select('id'), on='id', how='left_anti').select(
            'id', 'name', 'segment', col('as_of_date').alias('effective_start'),
            lit(None).cast('string').alias('effective_end'), lit(True).alias('is_current')
        )
        return unchanged.unionByName(closed).unionByName(new_versions).unionByName(inserts)


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("implement_slowly_changing_dimension_scd_type_2")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [(1, 'Alice', 'premium', '2026-04-07'), (2, 'Bob', 'basic', '2026-04-07')]
    columns = ['id', 'name', 'segment', 'as_of_date']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
