"""
Problem: Optimize file size while writing

Description:
Prepare DataFrame to avoid tiny output files by controlling partition count.

Expected Output:
DataFrame ready for write with optimal partitioning.

Pattern: Optimization
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
        target_partitions = max(1, min(8, df.rdd.getNumPartitions()))
        return df.coalesce(target_partitions)


if __name__ == "__main__":
    spark = SparkSession.builder         .appName("optimize_file_size_while_writing")         .getOrCreate()

    # Sample input data (realistic small dataset)
    data = [(1, 'cat_1'), (2, 'cat_2'), (3, 'cat_0'), (4, 'cat_1'), (5, 'cat_2'), (6, 'cat_0'), (7, 'cat_1'), (8, 'cat_2'), (9, 'cat_0'), (10, 'cat_1'), (11, 'cat_2'), (12, 'cat_0'), (13, 'cat_1'), (14, 'cat_2'), (15, 'cat_0'), (16, 'cat_1'), (17, 'cat_2'), (18, 'cat_0'), (19, 'cat_1'), (20, 'cat_2'), (21, 'cat_0'), (22, 'cat_1'), (23, 'cat_2'), (24, 'cat_0'), (25, 'cat_1'), (26, 'cat_2'), (27, 'cat_0'), (28, 'cat_1'), (29, 'cat_2'), (30, 'cat_0'), (31, 'cat_1'), (32, 'cat_2'), (33, 'cat_0'), (34, 'cat_1'), (35, 'cat_2'), (36, 'cat_0'), (37, 'cat_1'), (38, 'cat_2'), (39, 'cat_0'), (40, 'cat_1'), (41, 'cat_2'), (42, 'cat_0'), (43, 'cat_1'), (44, 'cat_2'), (45, 'cat_0'), (46, 'cat_1'), (47, 'cat_2'), (48, 'cat_0'), (49, 'cat_1'), (50, 'cat_2'), (51, 'cat_0'), (52, 'cat_1'), (53, 'cat_2'), (54, 'cat_0'), (55, 'cat_1'), (56, 'cat_2'), (57, 'cat_0'), (58, 'cat_1'), (59, 'cat_2'), (60, 'cat_0'), (61, 'cat_1'), (62, 'cat_2'), (63, 'cat_0'), (64, 'cat_1'), (65, 'cat_2'), (66, 'cat_0'), (67, 'cat_1'), (68, 'cat_2'), (69, 'cat_0'), (70, 'cat_1'), (71, 'cat_2'), (72, 'cat_0'), (73, 'cat_1'), (74, 'cat_2'), (75, 'cat_0'), (76, 'cat_1'), (77, 'cat_2'), (78, 'cat_0'), (79, 'cat_1'), (80, 'cat_2'), (81, 'cat_0'), (82, 'cat_1'), (83, 'cat_2'), (84, 'cat_0'), (85, 'cat_1'), (86, 'cat_2'), (87, 'cat_0'), (88, 'cat_1'), (89, 'cat_2'), (90, 'cat_0'), (91, 'cat_1'), (92, 'cat_2'), (93, 'cat_0'), (94, 'cat_1'), (95, 'cat_2'), (96, 'cat_0'), (97, 'cat_1'), (98, 'cat_2'), (99, 'cat_0'), (100, 'cat_1')]
    columns = ['id', 'category']

    df = spark.createDataFrame(data, columns)

    sol = Solution()
    result = sol.solve(df)

    result.show(truncate=False)
    spark.stop()
