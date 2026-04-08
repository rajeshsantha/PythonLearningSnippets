# Python Coding Interview Questions (3–4 Years Experience)

Below are **Python-only** coding interview questions structured into **Easy**, **Medium**, **Advanced**, and **Real-World Data Engineering** levels. Each row now includes a suggested **Function / Class name** and an **Expected Time** estimate so you can plan practice sessions.

---

| ID | Difficulty | Question | Function / Class Name | Example | Expected Time | Code |
|----|------------|----------|------------------------|---------|---------------|------|
| 1  | Easy | Reverse words in a sentence | `reverse_words()` | "I love Python" → "Python love I" | 5–10 min | [View](./easy/strings/reverse_words_in_a_sentence.py) |
| 2  | Easy | Find second largest number (no sorting) | `second_largest()` | — | 10–15 min | [View](./easy/arrays/find_second_largest_number_no_sorting.py) |
| 3  | Easy | Remove duplicates while preserving order | `remove_duplicates_ordered()` | — | 10 min | [View](./easy/arrays/remove_duplicates_while_preserving_order.py) |
| 4  | Easy | Check if a string is a palindrome (ignore symbols) | `is_palindrome()` | "A man, a plan..." | 10–15 min | [View](./easy/two_pointers/check_if_a_string_is_a_palindrome_ignore_symbols.py) |
| 5  | Easy | Count character frequency in a string | `char_frequency()` | — | 5–10 min | [View](./easy/hashing/count_character_frequency_in_a_string.py) |
| 6  | Easy | Merge two sorted lists without built-ins | `merge_sorted_lists()` | — | 10–20 min | [View](./easy/two_pointers/merge_two_sorted_lists_without_built_ins.py) |
| 7  | Easy | Unique elements in order of appearance | `unique_ordered()` | — | 10 min | [View](./easy/hashing/unique_elements_in_order_of_appearance.py) |
| 8  | Easy | Sort list of tuples by second value | `sort_by_second()` | [(1,5),(2,3)] | 10 min | [View](./easy/arrays/sort_list_of_tuples_by_second_value.py) |
| 9  | Easy | Check if two strings are anagrams | `are_anagrams()` | "listen"/"silent" | 10–15 min | [View](./easy/hashing/check_if_two_strings_are_anagrams.py) |
| 10 | Easy | Flatten list by one level | `flatten_once()` | [[1,2],[3,4]] → [1,2,3,4] | 5–10 min | [View](./easy/arrays/flatten_list_by_one_level.py) |
| 11 | Medium | Flatten deeply nested list | `flatten_deep()` | [1,[2,[3]]] | 20–30 min | [View](./medium/recursion/flatten_deeply_nested_list.py) |
| 12 | Medium | Group elements by frequency | `group_frequency()` | {"a":3,"b":2} | 15–20 min | [View](./medium/hashing/group_elements_by_frequency.py) |
| 13 | Medium | Top 3 frequent elements | `top_k_frequent()` | — | 20–30 min | [View](./medium/heap/top_3_frequent_elements.py) |
| 14 | Medium | Build your own groupBy | `group_by_key()` | — | 20 min | [View](./medium/hashing/build_your_own_groupby.py) |
| 15 | Medium | Compute running average | `running_average()` | [10,20,30] → [10,15,20] | 15–20 min | [View](./medium/arrays/compute_running_average.py) |
| 16 | Medium | Common elements between two lists | `common_elements()` | — | 15–20 min | [View](./medium/hashing/common_elements_between_two_lists.py) |
| 17 | Medium | Convert list of dicts → dict of lists | `listdict_to_dictlist()` | {"id":[1,2]} | 15–25 min | [View](./medium/hashing/convert_list_of_dicts_to_dict_of_lists.py) |
| 18 | Medium | Count "error" lines in huge file | `count_error_lines()` | — | 15–20 min | [View](./medium/real_world/count_error_lines_in_huge_file.py) |
| 19 | Medium | Extract digits from string | `extract_digits()` | "ab12c3" → "123" | 10–15 min | [View](./medium/strings/extract_digits_from_string.py) |
| 20 | Medium | Sort list of dicts by date | `sort_by_date()` | — | 20–30 min | [View](./medium/arrays/sort_list_of_dicts_by_date.py) |
| 21 | Advanced | Implement LRU cache | `class LRUCache` | — | 45–60 min | [View](./advanced/design/implement_lru_cache.py) |
| 22 | Advanced | Caching decorator | `@memoize` | — | 30–45 min | [View](./advanced/design/caching_decorator.py) |
| 23 | Advanced | Retry decorator | `@retry(times=3)` | — | 20–30 min | [View](./advanced/design/retry_decorator.py) |
| 24 | Advanced | Implement map & filter using generators | `my_map()`, `my_filter()` | — | 25–35 min | [View](./advanced/design/implement_map_and_filter_using_generators.py) |
| 25 | Advanced | Flatten nested JSON | `flatten_json()` | {"id":1,"info":{}} | 30–45 min | [View](./advanced/recursion/flatten_nested_json.py) |
| 26 | Advanced | CSV → compute min/avg/max | `csv_stats()` | — | 25–40 min | [View](./advanced/real_world/csv_to_compute_min_avg_max.py) |
| 27 | Advanced | Chunk list into N parts | `chunk_list()` | chunk([1,2,3,4],2) | 15–25 min | [View](./advanced/arrays/chunk_list_into_n_parts.py) |
| 28 | Advanced | Binary search | `binary_search()` | — | 15–25 min | [View](./advanced/arrays/binary_search.py) |
| 29 | Advanced | Detect loop in linked list | `detect_cycle()` | Floyd's algorithm | 20–30 min | [View](./advanced/linked_list/detect_loop_in_linked_list.py) |
| 30 | Advanced | Serialize/Deserialize binary tree | `serialize_tree()`, `deserialize_tree()` | — | 30–45 min | [View](./advanced/tree_graph/serialize_and_deserialize_binary_tree.py) |
| 31 | Real-world | Clean CSV (ETL task) | `clean_csv()` | strip/lowercase | 30–50 min | [View](./advanced/real_world/clean_csv_etl_task.py) |
| 32 | Real-world | Top N IPs from logs | `top_ips()` | — | 20–35 min | [View](./advanced/real_world/top_n_ips_from_logs.py) |
| 33 | Real-world | Split large file | `split_file()` | — | 25–40 min | [View](./advanced/real_world/split_large_file.py) |
| 34 | Real-world | Validate JSON schema | `validate_schema()` | — | 25–40 min | [View](./advanced/real_world/validate_json_schema.py) |
| 35 | Real-world | Compare two JSON files | `compare_json()` | — | 30–45 min | [View](./advanced/real_world/compare_two_json_files.py) |
| 36 | Real-world | Detect duplicates using composite key | `find_duplicates()` | (id, date) | 20–30 min | [View](./advanced/hashing/detect_duplicates_using_composite_key.py) |
| 37 | Real-world | SQL-style GROUP BY + AGG | `group_by_agg()` | ("A",10) | 25–40 min | [View](./advanced/hashing/sql_style_group_by_and_agg.py) |
| 38 | Real-world | Sliding-window max | `sliding_window_max()` | — | 25–40 min | [View](./advanced/sliding_window/sliding_window_max.py) |
| 39 | Real-world | Compute user sessions | `sessionize()` | gap > 30 mins | 25–40 min | [View](./advanced/real_world/compute_user_sessions.py) |
| 40 | Real-world | CLI Task Manager | `class TaskManager` | add/list/done | 40–60 min | [View](./advanced/design/cli_task_manager.py) |

---

## ✔ What Next?
Ask for:
- Full solutions for each question  
- GitHub-ready project structure  
- Test cases (pytest)  
- Beginner, Medium & Advanced learning roadmap  
