| Problem | Difficulty | Pattern | Description | Expected Output | Code |
|--------|-----------|--------|------------|----------------|------|
| Remove duplicate records using primary key | Easy | Deduplication | Given a DataFrame with duplicate records based on `id`, keep the latest record based on timestamp | DataFrame with unique `id` | [View](./easy/data_cleaning/remove_duplicate_records_using_primary_key.py) |
| Count records per category | Easy | Aggregation | Given a DataFrame with `category`, count number of records per category | category, count | [View](./easy/aggregation/count_records_per_category.py) |
| Filter null or invalid records | Easy | Data Cleaning | Remove rows where critical columns (id, name) are null or empty | Cleaned DataFrame | [View](./easy/data_cleaning/filter_null_or_invalid_records.py) |
| Convert JSON column to structured columns | Easy | JSON Parsing | Parse a JSON string column into multiple columns using schema | Flattened DataFrame | [View](./easy/transformation/convert_json_column_to_structured_columns.py) |
| Join two DataFrames (inner join) | Easy | Join | Join orders and customers on customer_id | Combined DataFrame | [View](./easy/join/join_two_dataframes_inner_join.py) |
| Find top N records per group | Medium | Window Function | Find top 3 highest salary employees per department | dept, employee, salary | [View](./medium/window/find_top_n_records_per_group.py) |
| Running total using window | Medium | Window Function | Calculate cumulative sum of sales per region ordered by date | region, date, running_total | [View](./medium/window/running_total_using_window.py) |
| Handle skewed join | Hard | Optimization | Join a large skewed dataset where one key dominates (e.g., null or 'unknown') | Optimized join avoiding skew | [View](./hard/optimization/handle_skewed_join.py) |
| Broadcast join optimization | Medium | Optimization | Optimize join when one dataset is small (<10MB) | Faster join execution | [View](./medium/optimization/broadcast_join_optimization.py) |
| Repartition vs Coalesce usage | Medium | Partitioning | Repartition a dataset to 10 partitions for parallel processing | Balanced partitions | [View](./medium/partitioning/repartition_vs_coalesce_usage.py) |
| Write incremental load (append + dedup) | Medium | Incremental Load | Load daily data into Delta table ensuring no duplicates | Updated Delta table | [View](./medium/cdc/write_incremental_load_append_dedup.py) |
| Implement CDC (Change Data Capture) | Hard | CDC | Merge source changes (insert/update/delete) into target Delta table | Updated target table | [View](./hard/cdc/implement_cdc_change_data_capture.py) |
| Late arriving data handling | Hard | Streaming/ETL | Handle late events using watermark in streaming job | Correct aggregated output | [View](./hard/streaming/late_arriving_data_handling.py) |
| Sliding window aggregation | Medium | Streaming | Calculate average clicks over last 10 minutes window | time_window, avg_clicks | [View](./medium/streaming/sliding_window_aggregation.py) |
| Detect duplicate events in stream | Medium | Streaming | Remove duplicate events using event_id in streaming | Deduplicated stream | [View](./medium/streaming/detect_duplicate_events_in_stream.py) |
| Handle streaming failure recovery | Hard | Streaming | Restart streaming job from checkpoint after failure | No data loss | [View](./hard/streaming/handle_streaming_failure_recovery.py) |
| Optimize large aggregation job | Hard | Optimization | Reduce shuffle during groupBy on large dataset | Optimized execution | [View](./hard/optimization/optimize_large_aggregation_job.py) |
| Explode nested array column | Easy | Transformation | Flatten array column into multiple rows | Expanded rows | [View](./easy/transformation/explode_nested_array_column.py) |
| Pivot data from rows to columns | Medium | Transformation | Convert transaction types into columns | Pivoted DataFrame | [View](./medium/transformation/pivot_data_from_rows_to_columns.py) |
| Unpivot columns to rows | Medium | Transformation | Convert multiple columns into key-value rows | Normalized DataFrame | [View](./medium/transformation/unpivot_columns_to_rows.py) |
| Handle null-safe joins | Medium | Join | Join datasets where keys may contain null values | Correct join output | [View](./medium/join/handle_null_safe_joins.py) |
| Optimize file size while writing | Medium | Optimization | Write parquet files with optimal file size (avoid small files) | Optimized file layout | [View](./medium/optimization/optimize_file_size_while_writing.py) |
| Partition data while writing | Easy | Partitioning | Write data partitioned by date column | Partitioned output | [View](./easy/partitioning/partition_data_while_writing.py) |
| Z-order optimization (Delta) | Hard | Optimization | Optimize Delta table for faster queries on specific columns | Faster query performance | [View](./hard/optimization/z_order_optimization_delta.py) |
| Cache vs persist usage | Medium | Optimization | Cache intermediate DataFrame reused multiple times | Faster execution | [View](./medium/optimization/cache_vs_persist_usage.py) |
| Identify and fix data skew in aggregation | Hard | Optimization | Detect skew in groupBy and fix using salting technique | Balanced aggregation | [View](./hard/optimization/identify_and_fix_data_skew_in_aggregation.py) |
| Read streaming data from Kafka | Medium | Streaming | Consume Kafka topic and parse JSON messages | Structured stream | [View](./medium/streaming/read_streaming_data_from_kafka.py) |
| Write streaming output to Delta | Medium | Streaming | Write stream output to Delta table with checkpointing | Durable data | [View](./medium/streaming/write_streaming_output_to_delta.py) |
| Handle schema evolution in Delta | Hard | Schema Evolution | Add new column in incoming data and merge with existing table | Updated schema | [View](./hard/schema_evolution/handle_schema_evolution_in_delta.py) |
| Implement slowly changing dimension (SCD Type 2) | Hard | Data Modeling | Track historical changes of records with effective dates | Historical table | [View](./hard/cdc/implement_slowly_changing_dimension_scd_type_2.py) |
| Find missing records between two datasets | Medium | Data Validation | Identify records present in source but missing in target | Missing records | [View](./medium/join/find_missing_records_between_two_datasets.py) |
| Optimize join with large datasets | Hard | Optimization | Join two large datasets efficiently using partitioning | Optimized join | [View](./hard/optimization/optimize_join_with_large_datasets.py) |
| Remove duplicates with window function | Medium | Deduplication | Keep latest record per id using row_number | Deduplicated output | [View](./medium/data_cleaning/remove_duplicates_with_window_function.py) |
| Compute sessionization from logs | Hard | Streaming | Group user activity into sessions based on inactivity gap | session_id, events | [View](./hard/streaming/compute_sessionization_from_logs.py) |
| Handle out-of-order data in stream | Hard | Streaming | Process events arriving out of order using watermark | Correct aggregation | [View](./hard/streaming/handle_out_of_order_data_in_stream.py) |
| Perform multi-column sorting | Easy | Transformation | Sort DataFrame by multiple columns (date desc, id asc) | Sorted DataFrame | [View](./easy/transformation/perform_multi_column_sorting.py) |
| Convert wide data to long format | Medium | Transformation | Normalize wide dataset into key-value pairs | Long format data | [View](./medium/transformation/convert_wide_data_to_long_format.py) |
| Optimize memory usage in Spark job | Hard | Optimization | Tune Spark configs to reduce OOM errors | Stable job execution | [View](./hard/optimization/optimize_memory_usage_in_spark_job.py) |
