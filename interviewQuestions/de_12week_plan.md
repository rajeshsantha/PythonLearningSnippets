# 12-Week Plan - Rajesh Santha - April 19th, 2026

## Overview
A structured 12-week curriculum designed to prepare you for data engineering roles. The plan progresses from foundational skills (SQL, Python) through intermediate concepts (ETL, data modeling) to advanced topics (system design, cloud architecture). Each week includes specific learning outcomes, practice projects, and interview prep.

**Target Roles:** Data Engineer, Analytics Engineer, ETL Developer, Platform Engineer

---

## PHASE 1: FOUNDATIONS (Weeks 1-4)

### Week 1: SQL Mastery Begins
**Duration:** 7-8 hours  
**Focus:** Core SQL and relational database concepts

**Topics:**
- SQL fundamentals (SELECT, WHERE, GROUP BY, HAVING, ORDER BY)
- JOINs (INNER, LEFT, RIGHT, FULL OUTER, CROSS)
- Subqueries and CTEs (Common Table Expressions)
- Window functions (ROW_NUMBER, RANK, LAG, LEAD, SUM OVER)
- Indexing basics and query optimization

**Deliverables:**

**LeetCode SQL Problems to Solve (Easy):**
- [175. Combine Two Tables](https://leetcode.com/problems/combine-two-tables/) — Basic LEFT JOIN
- [176. Second Highest Salary](https://leetcode.com/problems/second-highest-salary/) — Subquery + NULL handling
- [182. Duplicate Emails](https://leetcode.com/problems/duplicate-emails/) — GROUP BY + HAVING
- [183. Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/) — LEFT JOIN + IS NULL
- [196. Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/) — DELETE with self-join
- [197. Rising Temperature](https://leetcode.com/problems/rising-temperature/) — Self-join on dates
- [577. Employee Bonus](https://leetcode.com/problems/employee-bonus/) — LEFT JOIN with NULL filter
- [584. Find Customer Referee](https://leetcode.com/problems/find-customer-referee/) — NULL-safe comparisons
- [595. Big Countries](https://leetcode.com/problems/big-countries/) — Basic SELECT + WHERE
- [620. Not Boring Movies](https://leetcode.com/problems/not-boring-movies/) — Filtering + ORDER BY

**LeetCode SQL Problems to Solve (Medium):**
- [177. Nth Highest Salary](https://leetcode.com/problems/nth-highest-salary/) — Parameterized subquery
- [178. Rank Scores](https://leetcode.com/problems/rank-scores/) — DENSE_RANK() vs RANK()
- [180. Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers/) — Self-join or window function
- [184. Department Highest Salary](https://leetcode.com/problems/department-highest-salary/) — DENSE_RANK() per partition
- [185. Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/) — DENSE_RANK() top-N per group
- [550. Game Play Analysis IV](https://leetcode.com/problems/game-play-analysis-iv/) — DATE logic + window functions
- [570. Managers with at Least 5 Direct Reports](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/) — Grouped JOIN
- [574. Winning Candidate](https://leetcode.com/problems/winning-candidate/) — Aggregation + JOIN
- [580. Count Student Number in Departments](https://leetcode.com/problems/count-student-number-in-departments/) — LEFT JOIN + COUNT
- [602. Friend Requests II: Who Has the Most Friends](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/) — UNION + COUNT

**Practice Writing These Queries from Scratch:**
1. Find all employees earning more than their manager's salary (self-join)
2. Calculate a running total of sales per month using `SUM() OVER(ORDER BY month)`
3. Find the top 3 products by revenue in each category using `DENSE_RANK() OVER(PARTITION BY category ORDER BY revenue DESC)`
4. Identify users who logged in on 3+ consecutive days (row number gap trick)
5. Pivot a table: show monthly revenue as columns (Jan, Feb, Mar…) using `CASE WHEN`
6. Deduplicate records: keep only the most recent row per `user_id` using `ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY created_at DESC)`
7. Calculate month-over-month revenue growth % using `LAG()`

**Full LeetCode SQL 50 Study Plan:** https://leetcode.com/studyplan/top-sql-50/

**Interview Prep:**
- Q: "Write a SQL query to find duplicate rows in a table."
  - *Expected:* `SELECT col, COUNT(*) FROM table GROUP BY col HAVING COUNT(*) > 1`
- Q: "What is the difference between `RANK()`, `DENSE_RANK()`, and `ROW_NUMBER()`?"
  - *Expected:* RANK skips numbers on ties, DENSE_RANK doesn't skip, ROW_NUMBER always unique
- Q: "Write a query to get the second highest salary."
  - *Expected:* `SELECT MAX(salary) FROM Employee WHERE salary < (SELECT MAX(salary) FROM Employee)`
- Q: "Explain the difference between INNER JOIN and LEFT JOIN with an example."
  - *Expected:* INNER returns matching rows only; LEFT returns all left rows + NULLs for non-matches
- Q: "How would you optimize a slow query?"
  - *Expected:* Check indexes, use EXPLAIN PLAN, avoid SELECT *, push filters before JOINs, partition large tables
- Q: "What is a CTE and when would you use it over a subquery?"
  - *Expected:* CTEs improve readability, allow recursion, can be referenced multiple times; subqueries are inline but harder to debug
- Q: "Write a query to find customers who placed orders in January but not February."
  - *Expected:* Use LEFT JOIN on February orders + WHERE feb.id IS NULL, or use EXCEPT/NOT IN

**Tools to Use:**
- PostgreSQL or MySQL (local setup)
- LeetCode SQL or HackerRank
- SQLZoo for interactive practice

---

### Week 2: Python for Data Engineering
**Duration:** 12-15 hours (extended — Python is foundational, don't rush it)  
**Focus:** Python from zero to data-engineering-ready

> **My Recommended Learning Approach:**  
> Don't try to "learn Python" in the abstract. Learn it by **solving data problems**. Every concept here is taught in the context of something a data engineer actually does: reading files, transforming records, handling errors, processing large datasets. Write code for every single concept — don't just read it.

---

#### 📚 CONCEPT BLOCK 1: Python Language Fundamentals (Days 1–2)

**1.1 — Variables, Data Types & Type Conversion**

Everything in Python is an object. Learn these types cold:

```python
# Primitive types
age = 25              # int
price = 19.99         # float
name = "Alice"        # str
is_active = True      # bool
nothing = None        # NoneType

# Type conversion (critical in data pipelines — CSV everything is a string!)
age_str = "25"
age_int = int(age_str)       # "25" → 25
price_str = str(19.99)       # 19.99 → "19.99"
flag = bool(0)               # 0 → False (0, "", None, [] are all falsy)
```

**Practice:** Given a list like `["25", "30.5", None, "abc", "10"]`, write a function that safely converts each to float, returns `None` for invalid values, and counts how many failed.

---

**1.2 — Strings & String Operations**

Data engineers clean messy strings constantly:

```python
s = "  Hello, World!  "
s.strip()               # → "Hello, World!"   (remove whitespace)
s.lower()               # → "hello, world!"
s.replace(",", "")      # → "  Hello World!  "
s.split(", ")           # → ["  Hello", "World!  "]
"hello".startswith("he") # → True

# f-strings (always use these, not .format() or %)
name = "Alice"
age = 25
print(f"User {name} is {age} years old")

# String slicing
s = "2024-01-15"
year = s[:4]      # "2024"
month = s[5:7]    # "01"
day = s[8:]       # "15"
```

**Practice:** Write a function `clean_phone(s)` that takes a phone string like `"(123) 456-7890"` or `"123.456.7890"` and returns `"1234567890"` (digits only).

---

**1.3 — Lists, Tuples, Sets, Dictionaries**

These are the workhorses of data transformation:

```python
# LIST — ordered, mutable, allows duplicates
records = [1, 2, 3, 2, 1]
records.append(4)           # add to end
records.pop(0)              # remove first element
records[1:3]                # slice → [2, 3]

# LIST COMPREHENSION — the most DE-useful Python syntax
prices = [10, 20, 30, 40, 50]
discounted = [p * 0.9 for p in prices if p > 15]  # → [18.0, 27.0, 36.0, 45.0]

# DICT — key-value store, O(1) lookup
user = {"id": 1, "name": "Alice", "age": 25}
user["email"] = "alice@example.com"    # add key
user.get("phone", "N/A")               # safe access with default
user.keys(), user.values(), user.items()

# DICT COMPREHENSION
names = ["Alice", "Bob", "Carol"]
name_lengths = {name: len(name) for name in names}  # → {"Alice": 5, ...}

# SET — unique values only, O(1) lookup
seen_ids = set()
seen_ids.add(1)
if 1 in seen_ids:   # O(1) — much faster than "if 1 in list"
    print("duplicate!")

# TUPLE — immutable, used for fixed records or function returns
row = (1, "Alice", 25)   # row[0]=1, row[1]="Alice"
```

**Practice Problems (write these without looking up answers):**
1. Given `records = [{"id":1,"val":10}, {"id":2,"val":20}, {"id":1,"val":30}]`, return a deduplicated list keeping the last occurrence of each `id`
2. Given a list of strings, return a dict of `{word: frequency}` using only dict comprehension and `get()`
3. Given two lists of user IDs, find: (a) IDs in both lists, (b) IDs only in list A, (c) IDs in either — use set operations

---

**1.4 — Control Flow: if/elif/else, for, while**

```python
# Conditional
status_code = 404
if status_code == 200:
    print("OK")
elif status_code == 404:
    print("Not Found")
else:
    print("Other error")

# For loops over iterables
for i, name in enumerate(["Alice", "Bob"]):
    print(f"{i}: {name}")          # 0: Alice, 1: Bob

for key, value in user.items():   # iterate dict
    print(f"{key} = {value}")

# While with break/continue
i = 0
while i < 10:
    if i % 2 == 0:
        i += 1
        continue    # skip even numbers
    print(i)
    i += 1

# Ternary (one-liner if/else)
label = "high" if price > 50 else "low"
```

**Practice:** Write a function that takes a list of dicts (CSV rows) and returns only rows where `age > 18`, `email` is not None, and `status == "active"` — using a for loop first, then rewrite with list comprehension.

---

**1.5 — Functions: Definition, Arguments, Return Values, Scope**

```python
# Basic function
def calculate_revenue(price, quantity, discount=0):
    """
    Calculates total revenue after discount.
    Args:
        price: unit price (float)
        quantity: number of units (int)
        discount: discount percentage 0-1 (float, default 0)
    Returns:
        float: total revenue
    """
    return price * quantity * (1 - discount)

# Call with positional or keyword args
calculate_revenue(10, 5)                    # 50.0
calculate_revenue(10, 5, discount=0.1)     # 45.0

# *args — variable positional arguments
def sum_all(*numbers):
    return sum(numbers)
sum_all(1, 2, 3, 4)   # → 10

# **kwargs — variable keyword arguments
def log_event(event_type, **metadata):
    print(f"Event: {event_type}, Data: {metadata}")
log_event("purchase", user_id=1, amount=99.9)

# Functions as first-class objects (pass them around!)
def apply_transform(data, transform_fn):
    return [transform_fn(x) for x in data]

apply_transform([1, 2, 3], lambda x: x * 2)  # → [2, 4, 6]
```

**Practice:** Write a function `transform_pipeline(data, *functions)` that applies a list of functions to data in sequence (like a mini ETL pipeline). Test with: strip whitespace → lowercase → remove punctuation.

---

**1.6 — Error Handling: try/except/finally**

Every production pipeline must handle errors gracefully:

```python
def safe_convert(value, target_type):
    try:
        return target_type(value)
    except (ValueError, TypeError) as e:
        print(f"Conversion failed for '{value}': {e}")
        return None
    finally:
        pass  # always runs — good for cleanup

# Raising custom errors
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError(f"Expected int, got {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"Age {age} is out of valid range")
    return age

# Custom exception class
class DataValidationError(Exception):
    def __init__(self, field, reason):
        super().__init__(f"Validation failed on '{field}': {reason}")
        self.field = field
```

**Practice:** Write a `parse_record(row: dict)` function that validates required fields (`id`, `name`, `email`, `created_at`), raises `DataValidationError` for missing/invalid fields, and returns a cleaned dict. Test with 5 different bad inputs.

---

**1.7 — File I/O: Reading & Writing Files**

```python
import csv, json, os

# Reading a CSV
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)   # each row is a dict
    for row in reader:
        print(row["name"], row["age"])

# Writing a CSV
fieldnames = ["id", "name", "revenue"]
with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows([{"id": 1, "name": "Alice", "revenue": 500}])

# Reading JSON
with open("data.json", "r") as f:
    data = json.load(f)           # file → dict/list
json_str = json.dumps(data, indent=2)  # dict → string

# Writing JSON (with pretty print)
with open("output.json", "w") as f:
    json.dump(data, f, indent=2, default=str)   # default=str handles dates

# Large file — read line by line (memory efficient!)
with open("huge_file.csv", "r") as f:
    for line in f:          # yields one line at a time
        process(line)
```

**Practice:** Write a script that reads `orders.csv`, filters for orders where `amount > 100`, enriches each row by looking up `customer_name` from `customers.json` (keyed by `customer_id`), and writes the enriched records to `enriched_orders.csv`.

---

#### 📚 CONCEPT BLOCK 2: Intermediate Python for DE (Days 3–4)

**2.1 — Generators & Iterators (Critical for large data!)**

```python
# Generator function — yields values one at a time (no memory spike)
def read_large_csv_in_chunks(filepath, chunk_size=10000):
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) == chunk_size:
                yield chunk       # yield pauses and returns the chunk
                chunk = []
        if chunk:
            yield chunk           # yield the last partial chunk

# Usage — processes 1TB file with O(chunk_size) memory
for chunk in read_large_csv_in_chunks("huge.csv", 10000):
    process_chunk(chunk)

# Generator expression (like list comprehension but lazy)
squares_gen = (x**2 for x in range(1_000_000))  # no memory used yet
next(squares_gen)  # → 0 (compute on demand)
```

**Mental model:** A list is a bucket that holds all items. A generator is a recipe that produces items one by one on demand — essential for processing files larger than RAM.

---

**2.2 — Decorators**

```python
import time, functools

# A decorator wraps a function to add behavior
def timer(func):
    @functools.wraps(func)       # preserves original function name/docs
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.2f}s")
        return result
    return wrapper

@timer
def load_data(filepath):
    # ... load logic ...
    pass

# Retry decorator — production DE staple
def retry(max_attempts=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"Attempt {attempt} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay * attempt)   # exponential backoff
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def fetch_from_api(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()
```

---

**2.3 — The `collections` Module**

```python
from collections import Counter, defaultdict, deque, namedtuple

# Counter — frequency counting
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = Counter(words)
count.most_common(2)    # → [("apple", 3), ("banana", 2)]

# defaultdict — dict that auto-initializes missing keys
orders_by_customer = defaultdict(list)
for order in orders:
    orders_by_customer[order["customer_id"]].append(order)
# No KeyError if customer_id is new!

# namedtuple — lightweight immutable record (like a typed row)
Record = namedtuple("Record", ["id", "name", "amount"])
r = Record(1, "Alice", 99.9)
r.name    # → "Alice"  (readable vs r[1])
```

---

**2.4 — Regular Expressions**

```python
import re

# Match patterns
email_pattern = r'^[\w.-]+@[\w.-]+\.\w{2,}$'
re.match(email_pattern, "user@example.com")   # match object (truthy)
re.match(email_pattern, "not-an-email")       # None (falsy)

# Extract groups
date_str = "Order placed on 2024-01-15 at 10:30"
match = re.search(r'(\d{4})-(\d{2})-(\d{2})', date_str)
if match:
    year, month, day = match.groups()    # ("2024", "01", "15")

# Find all matches
text = "IDs: 123, 456, 789"
ids = re.findall(r'\d+', text)           # → ["123", "456", "789"]

# Substitute
cleaned = re.sub(r'[^\w\s]', '', "Hello, World!")  # → "Hello World"
```

**Practice:** Write a function `parse_log_line(line)` that parses a log line like `"2024-01-15 10:30:45 ERROR [pipeline.py:42] - NullPointerException"` and returns a dict with `{date, time, level, file, line_number, message}`.

---

**2.5 — Modules & Packages**

```python
# Standard library modules you must know for DE
import os           # file paths, env vars: os.path.exists(), os.getenv()
import sys          # command-line args: sys.argv
import json         # JSON serialise/deserialise
import csv          # CSV reading/writing
import logging      # proper logging (not print!)
import datetime     # date arithmetic
import pathlib      # modern file paths: Path("data") / "input.csv"
import re           # regex
import time         # sleep, timing
import functools    # wraps, reduce
from typing import List, Dict, Optional, Tuple   # type hints

# Setting up logging (do this in every script)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(),                     # console
        logging.FileHandler("pipeline.log")          # file
    ]
)
logger = logging.getLogger(__name__)

logger.info("Pipeline started")
logger.warning("Null values detected in column: age")
logger.error("Failed to connect to database", exc_info=True)
```

---

#### 📚 CONCEPT BLOCK 3: Pandas & NumPy for Data Engineering (Days 4–5)

**3.1 — NumPy Essentials**

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr * 2                    # → [2, 4, 6, 8, 10] (vectorized, fast)
arr[arr > 3]               # → [4, 5] (boolean indexing)
np.mean(arr)               # → 3.0
np.where(arr > 3, "high", "low")   # → ["low","low","low","high","high"]
```

**Why NumPy matters in DE:** Pandas is built on top of NumPy. Vectorized NumPy operations on arrays are 10-100x faster than Python for loops.

---

**3.2 — Pandas: The DE Workhorse**

Learn these in order. Each builds on the previous.

```python
import pandas as pd

# --- CREATION ---
df = pd.read_csv("orders.csv", parse_dates=["order_date"])
df = pd.read_json("data.json")
df = pd.DataFrame([{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}])

# --- INSPECTION ---
df.shape          # (rows, cols)
df.dtypes         # column data types
df.head(5)        # first 5 rows
df.info()         # non-null counts + dtypes
df.describe()     # stats: mean, std, min, max per numeric column
df.isnull().sum() # count NULLs per column

# --- SELECTION ---
df["name"]                         # single column → Series
df[["name", "age"]]                # multiple columns → DataFrame
df[df["age"] > 25]                 # filter rows
df.loc[0:4, "name":"age"]          # label-based slice
df.iloc[0:4, 1:3]                  # position-based slice

# --- CLEANING ---
df.dropna(subset=["email"])                    # drop rows where email is NULL
df["age"].fillna(df["age"].median())           # fill NULLs with median
df.drop_duplicates(subset=["user_id"])         # remove duplicate rows
df["name"] = df["name"].str.strip().str.lower() # clean string column
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")  # coerce bad values to NaN

# --- TRANSFORMATION ---
df["revenue"] = df["price"] * df["quantity"]  # new column
df["category"] = df["amount"].apply(
    lambda x: "high" if x > 100 else "low"
)
df.rename(columns={"amt": "amount"}, inplace=True)

# --- AGGREGATION ---
df.groupby("category")["revenue"].sum()           # sum revenue per category
df.groupby("date").agg(
    total_orders=("id", "count"),
    total_revenue=("amount", "sum"),
    avg_order=("amount", "mean")
)

# --- JOINS (most important!) ---
orders = pd.read_csv("orders.csv")
customers = pd.read_csv("customers.csv")
merged = orders.merge(customers, on="customer_id", how="left")  # LEFT JOIN
# how options: "inner", "left", "right", "outer"

# --- SORTING ---
df.sort_values("revenue", ascending=False).head(10)   # top 10

# --- PIVOT ---
pivot = df.pivot_table(
    values="revenue",
    index="region",
    columns="product_category",
    aggfunc="sum",
    fill_value=0
)

# --- WINDOW FUNCTIONS (Pandas equivalent) ---
df["running_total"] = df.groupby("customer_id")["amount"].cumsum()
df["rank"] = df.groupby("category")["revenue"].rank(method="dense", ascending=False)
df["prev_month_rev"] = df.groupby("product")["revenue"].shift(1)  # like LAG()

# --- WRITING OUTPUT ---
df.to_csv("output.csv", index=False)
df.to_parquet("output.parquet", engine="pyarrow")
df.to_json("output.json", orient="records", lines=True)
```

---

**3.3 — Pandas Performance Tips**

```python
# BAD — apply with lambda on every row (slow Python loop)
df["doubled"] = df["amount"].apply(lambda x: x * 2)

# GOOD — vectorized operation (NumPy under the hood)
df["doubled"] = df["amount"] * 2

# BAD — iterrows (extremely slow for large DataFrames)
for index, row in df.iterrows():
    print(row["name"])

# GOOD — vectorized or use itertuples() if you must loop
for row in df.itertuples():
    print(row.name)

# Read large CSV in chunks
chunks = []
for chunk in pd.read_csv("huge.csv", chunksize=100_000):
    processed = chunk[chunk["status"] == "active"]
    chunks.append(processed)
result = pd.concat(chunks, ignore_index=True)
```

---

#### 📚 CONCEPT BLOCK 4: OOP Basics for DE (Day 5)

```python
class DataPipeline:
    """Base pipeline class."""
    
    def __init__(self, source: str, target: str):
        self.source = source
        self.target = target
        self.logger = logging.getLogger(self.__class__.__name__)
        self._records_processed = 0
    
    def extract(self) -> pd.DataFrame:
        raise NotImplementedError("Subclasses must implement extract()")
    
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError("Subclasses must implement transform()")
    
    def load(self, df: pd.DataFrame) -> None:
        raise NotImplementedError("Subclasses must implement load()")
    
    def run(self):
        self.logger.info(f"Starting pipeline: {self.source} → {self.target}")
        df = self.extract()
        df = self.transform(df)
        self.load(df)
        self.logger.info(f"Pipeline complete. Records processed: {self._records_processed}")


class CSVToPostgresPipeline(DataPipeline):
    """Concrete pipeline: reads CSV, cleans, loads to Postgres."""
    
    def extract(self) -> pd.DataFrame:
        df = pd.read_csv(self.source, parse_dates=["created_at"])
        self.logger.info(f"Extracted {len(df)} rows from {self.source}")
        return df
    
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.dropna(subset=["email", "id"])
        df["email"] = df["email"].str.strip().str.lower()
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
        self._records_processed = len(df)
        return df
    
    def load(self, df: pd.DataFrame) -> None:
        # df.to_sql(self.target, con=engine, if_exists="replace", index=False)
        df.to_csv(f"{self.target}.csv", index=False)  # simplified for now
```

---

#### 🎯 PRACTICE PROBLEMS — Graduated Difficulty

**Level 1 — Beginner (Day 1–2, pure Python):**
1. Write a function `is_palindrome(s)` — ignore spaces and case
2. Write a function that counts word frequencies in a string and returns the top 3 as a list of `(word, count)` tuples
3. Given a list of integers, return a new list with duplicates removed and order preserved
4. Write a function `safe_divide(a, b)` that returns `None` instead of raising `ZeroDivisionError`
5. Given a list of dicts `[{"name": "Alice", "score": 85}, ...]`, sort them by `score` descending

**Level 2 — Intermediate (Day 3–4, files + data structures):**
1. Read `orders.csv`. Group orders by `customer_id`. For each customer, calculate: total orders, total spend, average order value. Write to `customer_summary.csv`
2. Read a JSON file containing a list of products with nested `{"product": {"category": {"name": "Electronics"}}}`. Flatten to `{"product_category_name": "Electronics"}` for every record
3. Write a function that detects duplicate records in a CSV (by `id` column) and produces two output files: `unique.csv` and `duplicates.csv`
4. Write a log parser that reads `app.log` line-by-line, extracts error lines, counts errors by module name, and writes a summary report

**Level 3 — Advanced (Day 5–6, Pandas + OOP):**
1. Build a `DataQualityChecker` class that accepts a DataFrame and a `rules` dict like `{"email": "not_null", "age": "positive", "status": "in:active,inactive"}`. Run all rules and return a report of which rows failed which checks
2. Write a chunked CSV processor that reads a 10M-row (simulate with 1M) sales CSV, filters for `region == "APAC"`, computes daily revenue totals, and writes a summary — all without loading the full file into memory
3. Implement an incremental load function: given `existing.parquet` and `new_records.csv`, merge them keeping only the latest version of each record (by `id` + `updated_at`), write back to `existing.parquet`

---

#### 🔗 LeetCode Problems — Ordered by Difficulty

**Absolute Basics — Start Here:**
- [2235. Add Two Integers](https://leetcode.com/problems/add-two-integers/) — just run Python, get comfortable with the interface
- [1. Two Sum](https://leetcode.com/problems/two-sum/) ⭐ — dict lookup, mirrors row deduplication by key
- [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) — set for O(1) membership; exact pattern for deduplication checks
- [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) — Counter usage
- [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/) — in-place list manipulation

**Core DE Patterns:**
- [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) ⭐ — grouping by transformed key (like `groupby` in Pandas)
- [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) ⭐ — `Counter.most_common(k)`, maps to "top N products by revenue"
- [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) — set-based O(n) solution, think about finding gaps in data sequences
- [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) — prefix/suffix pattern, prefix sums appear in running totals

**Sliding Window (maps to streaming aggregations):**
- [643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) — fixed-size window (7-day rolling average)
- [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) ⭐ — dynamic window; think session detection
- [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) — prefix sum + hash map

**Intervals (maps to time-range merging in scheduling/pipelines):**
- [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) ⭐ — merge overlapping time windows; classic in pipeline scheduling
- [57. Insert Interval](https://leetcode.com/problems/insert-interval/) — insert a new job window into an existing schedule
- [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) — find minimum intervals to remove (schedule conflict resolution)

**Topological Sort (maps directly to DAG/Airflow task ordering):**
- [207. Course Schedule](https://leetcode.com/problems/course-schedule/) ⭐ — detect cycles in a DAG (Airflow DAG validation!)
- [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) ⭐ — return the execution order of tasks

**🐼 LeetCode 30 Days of Pandas (DE-Specific — do ALL 30):**
- https://leetcode.com/studyplan/30-days-of-pandas/
- Covers: `groupby`, `merge`, `fillna`, `pivot_table`, string ops, `apply`, filtering, sorting, window functions in Pandas

---

#### 🗺️ My Recommended Learning Order for a Python Beginner in DE

Follow this exact sequence — don't skip ahead:

```
Day 1:  Variables → Strings → Lists → Dicts → Practice Level 1 (Q1–3)
Day 2:  Loops → Functions → File I/O → LeetCode: Two Sum, Contains Duplicate
Day 3:  Error Handling → Generators → Decorators → Practice Level 1 (Q4–5), Level 2 (Q1)
Day 4:  collections module → Regex → LeetCode: Group Anagrams, Top K Frequent
Day 5:  NumPy basics → Pandas (Concept 3.1–3.2) → LeetCode 30 Days of Pandas (first 10)
Day 6:  Pandas advanced (joins, window, pivot) → Practice Level 2 (Q2–4)
Day 7:  OOP basics → Practice Level 3 (Q1) → LeetCode: Merge Intervals, Course Schedule
```

**Key mindset rules:**
1. **Type everything yourself** — no copy-paste from solutions. Muscle memory matters.
2. **Break things intentionally** — pass wrong types, empty lists, None values. Learn what fails.
3. **Read error messages carefully** — `TypeError`, `KeyError`, `AttributeError` each tell you exactly what's wrong.
4. **After solving a LeetCode problem**, ask: "When would a data engineer face this exact problem with real data?"
5. **Write docstrings for every function** — practice explaining what your code does.

---

**Interview Prep:**
- Q: "How would you handle missing data in a Pandas DataFrame?"
  - *Expected:* Depends on context. `df.dropna(subset=["critical_col"])` for required fields. `df.fillna(df.median())` for numeric imputation. `df["date"].fillna(method="ffill")` for time-series. Always log what was dropped/filled and how many rows were affected.
- Q: "Write a function to validate email addresses in a dataset."
  - *Expected:* `import re; pattern = r'^[\w.-]+@[\w.-]+\.\w{2,}$'; bool(re.match(pattern, email))`
- Q: "Explain the difference between a list and a generator."
  - *Expected:* A list materializes all items in memory at once. A generator uses `yield` to produce items lazily — essential for processing files larger than RAM. Generator expression: `(x for x in range(1M))` vs list: `[x for x in range(1M)]`
- Q: "How do you process a 10GB CSV file in Python without running out of memory?"
  - *Expected:* `pd.read_csv(path, chunksize=100_000)` returns an iterator. Process each chunk independently. Alternatively, use Dask (`dd.read_csv()`) which is drop-in Pandas but distributed, or PySpark for cluster-scale.
- Q: "What is the difference between `apply()` and vectorized Pandas operations?"
  - *Expected:* `apply()` runs a Python function row-by-row in a Python loop — slow. Vectorized ops (`df["col"] * 2`) use NumPy array operations — 10–100x faster. Rule: always prefer built-in Pandas/NumPy operations over `apply()`.
- Q: "What are `*args` and `**kwargs`?"
  - *Expected:* `*args` collects extra positional arguments as a tuple; `**kwargs` collects extra keyword arguments as a dict. Used to write flexible functions that accept variable inputs — common in decorators and utility helpers.
- Q: "Explain Python's `with` statement."
  - *Expected:* Implements the context manager protocol (`__enter__`/`__exit__`). Guarantees the resource (file, DB connection, lock) is properly closed even if an exception occurs — equivalent to try/finally but cleaner.

**Tools to Use:**
- Python 3.10+
- Jupyter Notebook / VS Code with Pylance extension
- [LeetCode 30 Days of Pandas](https://leetcode.com/studyplan/30-days-of-pandas/)
- [Real Python tutorials](https://realpython.com) — best free Python learning resource
- Pandas documentation: https://pandas.pydata.org/docs/
- Book: *Automate the Boring Stuff with Python* (free online) — practical, not academic

---

### Week 3: Relational Databases & Data Modeling
**Duration:** 8-9 hours  
**Focus:** Database design principles and normalization

**Topics:**
- Entity-Relationship (ER) modeling
- Database normalization (1NF, 2NF, 3NF, BCNF)
- Keys (Primary, Foreign, Composite)
- Constraints (UNIQUE, NOT NULL, CHECK)
- Denormalization trade-offs
- Star schema and dimensional modeling intro

**Deliverables:**

**Design These ER Diagrams from Scratch (then implement in PostgreSQL):**
1. **E-Commerce System:** Entities: `customers`, `products`, `categories`, `orders`, `order_items`, `suppliers`. Relationships: customers place many orders; orders have many order_items; products belong to categories. Implement with proper FK constraints and indexes.
2. **Hotel Booking System:** Entities: `guests`, `rooms`, `room_types`, `bookings`, `payments`. Handle many-to-many between guests and rooms via bookings.
3. **Social Media Platform:** Entities: `users`, `posts`, `comments`, `likes`, `followers`. Handle self-referential many-to-many for followers.

**Normalization Practice Exercise:**
Given this flat table — normalize it to 3NF:
```
OrderID | CustomerName | CustomerCity | ProductName | ProductPrice | Quantity
```
- Identify all functional dependencies
- Split into: `Customers(id, name, city)`, `Products(id, name, price)`, `Orders(id, customer_id, date)`, `OrderItems(order_id, product_id, quantity)`
- Explain what anomalies the normalized form prevents

**SQL Schema Design Questions to Answer:**
1. Design a `users` table that tracks when a user's email changes over time (hint: versioning)
2. Design a tagging system where posts can have many tags and tags can belong to many posts
3. How would you store a product's price history (changing price over time)?
4. Design a table structure for a multi-tenant SaaS application where each tenant's data must be isolated

**Interview Prep:**
- Q: "Design a database schema for an e-commerce platform."
  - *Expected:* Describe entities (customers, orders, products, order_items), relationships, PKs/FKs, indexes on `customer_id`, `product_id`, `created_at`; mention 3NF normalization.
- Q: "What is the difference between normalization and denormalization?"
  - *Expected:* Normalization removes redundancy (OLTP, data integrity); denormalization adds redundancy for read speed (OLAP, fewer JOINs needed)
- Q: "When would you break normalization rules?"
  - *Expected:* In analytical/reporting databases (data warehouses), or when query performance is critical and joins become too expensive at scale
- Q: "What is a composite key? Give an example."
  - *Expected:* A PK made of 2+ columns — e.g., in `order_items(order_id, product_id)`, neither alone is unique but together they are
- Q: "Explain the difference between a 1NF, 2NF, and 3NF violation with a concrete example."
  - *Expected:* 1NF: non-atomic values (e.g., `tags = 'sql,python'`); 2NF: partial dependency on part of composite key; 3NF: transitive dependency (non-key depends on non-key)
- Q: "What indexes would you add to an orders table queried frequently by `customer_id` and `created_at`?"
  - *Expected:* Composite index on `(customer_id, created_at DESC)` for range + filter queries

**Tools to Use:**
- Lucidchart or Draw.io for ER diagrams
- PostgreSQL for implementation
- SQLAlchemy (Python ORM) for schema definition

---

### Week 4: Foundational Project & Review
**Duration:** 9-10 hours  
**Focus:** Consolidate Weeks 1-3 with a practical project

**Deliverables:**

**Project: E-Commerce Analytics Pipeline**
- **Objective:** Ingest raw CSV data into a normalized database, transform it, and generate analytical queries
- **Steps:**
  1. Design ER diagram for an e-commerce database (users, products, orders, order_items)
  2. Create normalized tables in PostgreSQL
  3. Write Python script to load sample CSV data (validate, handle errors, log progress)
  4. Write 10+ analytical SQL queries (top products, customer lifetime value, monthly revenue trends)
  5. Create a Python script that generates a weekly report

- **Expected Output:** GitHub repo with schema, data loader, SQL queries, and report generator

**Interview Prep:**
- Mock interview: Database design + SQL optimization
- Review Week 1-3 concepts
- Prepare 10 behavioral questions (why data engineering, challenges overcome)

**Milestone Checkpoint:**
- [ ] Can design normalized database schemas
- [ ] Write efficient SQL queries with JOINs and window functions
- [ ] Write Python scripts that handle data I/O and errors
- [ ] Understand ER modeling and data modeling principles

---

## PHASE 2: INTERMEDIATE CONCEPTS (Weeks 5-8)

### Week 5: ETL & Data Pipelines
**Duration:** 8-9 hours  
**Focus:** Building and orchestrating data pipelines

**Topics:**
- ETL vs ELT concepts
- Extract patterns (APIs, databases, file systems)
- Transform logic (filtering, joining, aggregating)
- Load strategies (batch, incremental, upsert)
- Data validation and quality checks
- Error handling and retries

**Deliverables:**

**ETL Coding Challenges to Build:**
1. **Idempotent Batch Loader:** Write a Python script that loads CSV files into PostgreSQL such that re-running it never creates duplicates — use `INSERT ... ON CONFLICT DO UPDATE` (upsert) with a watermark timestamp
2. **Data Quality Gate:** Build a validation layer that checks: (a) schema matches expected columns, (b) no NULLs in required fields, (c) values in allowed enums, (d) date formats are valid. Route bad rows to a quarantine table, good rows to production
3. **Incremental Load:** Implement logic that tracks `last_processed_timestamp` in a control table and only extracts records newer than the last run
4. **Deduplication Transform:** Given event logs with duplicate `event_id`, write a transform that keeps only the first occurrence per `event_id` ordered by `received_at`
5. **Bronze → Silver → Gold:** Build a 3-stage pipeline: Bronze (raw CSV as-is), Silver (cleaned: cast types, strip whitespace, fill NULLs), Gold (aggregated: daily revenue per product)

**Scenario-Based Questions to Practice Answering:**
- *"Design a pipeline to process daily e-commerce CSV files. The pipeline frequently fails due to malformed dates. Walk me through your design."* — Answer should cover: staging → validation → quarantine → idempotent load → monitoring
- *"Your ETL job ran twice due to a bug, causing duplicate rows in the warehouse. How do you detect and fix this?"* — Answer: row count comparison, checksum, deduplicate with `ROW_NUMBER()` CTE
- *"How would you re-process 6 months of historical data without overloading the system?"* — Answer: backfill in date partitions, use Airflow templated dates `{{ ds }}`

**Interview Prep:**
- Q: "Design an ETL pipeline for real-time event streaming."
  - *Expected:* Source events → Kafka topic → Stream processor (Spark Structured Streaming or Flink) → validate/transform → write to data warehouse; mention exactly-once semantics, DLQ for bad events
- Q: "How would you handle a data quality issue discovered mid-pipeline?"
  - *Expected:* Quarantine bad records, alert on-call, let valid records proceed (don't halt entire pipeline), log root cause, fix upstream + backfill
- Q: "Explain upsert vs insert logic."
  - *Expected:* INSERT adds new rows; UPSERT (`INSERT ... ON CONFLICT DO UPDATE`) updates if key exists — critical for idempotent loads where records can change
- Q: "What is the difference between ETL and ELT?"
  - *Expected:* ETL transforms before loading (legacy, on-prem); ELT loads raw first then transforms in warehouse (modern cloud: Snowflake, BigQuery) — better for schema flexibility and reprocessing
- Q: "How do you ensure your pipeline is idempotent?"
  - *Expected:* Use upsert on unique keys, partition target table by date and overwrite partition, use watermark/control table, avoid append-only writes without deduplication

**Tools to Use:**
- Python (pandas, sqlalchemy)
- PostgreSQL for source/target
- Logging module for pipeline observability
- Pytest for testing

---

### Week 6: Apache Spark & Distributed Processing
**Duration:** 9-10 hours  
**Focus:** Scalable data processing framework

**Topics:**
- Spark architecture (Driver, Executors, Partitions)
- RDD vs DataFrames vs Datasets
- Lazy evaluation and actions
- Transformations (map, filter, flatMap, groupByKey, join, reduce)
- SQL on Spark (SparkSQL)
- Performance tuning (partitioning, caching, shuffles)
- Spark on distributed cluster basics

**Deliverables:**

**PySpark Coding Exercises to Complete:**
1. **Top-N per Group:** Given a sales DataFrame with `(product_id, category, revenue)`, find the top 3 revenue products in each category using `Window.partitionBy("category").orderBy(F.desc("revenue"))` and `F.dense_rank()`
2. **Deduplication:** Given a DataFrame with duplicate `user_id` rows, keep only the row with the latest `updated_at` using `ROW_NUMBER()` window function
3. **Broadcast Join Optimization:** Join a large transactions DataFrame (100M rows) with a small country lookup table (200 rows) — implement using `F.broadcast(small_df)` and explain why it avoids shuffle
4. **Handle Data Skew:** You have a join on `user_id` where one user has 40% of all rows. Implement salting: add a random suffix `0..9` to the skewed key, explode on the other side, join, then de-salt
5. **Aggregation Pipeline:** Read raw e-commerce events from Parquet, filter for `event_type = 'purchase'`, group by `(date, product_id)`, compute `total_revenue`, `avg_order_value`, `count_orders`, write output partitioned by `date`
6. **Schema Evolution:** Union two DataFrames with different schemas using `unionByName(df1, df2, allowMissingColumns=True)`
7. **SparkSQL:** Register a DataFrame as a temp view and write a SQL query using `DENSE_RANK()` over a window

**Concept Questions to Be Able to Explain:**
- What happens when you call `.cache()` on a DataFrame? When would you NOT cache?
- Explain the difference between `repartition(n)` and `coalesce(n)` — which causes a shuffle?
- What is a "shuffle" in Spark? Which operations trigger shuffles? (groupBy, join, repartition)
- What is the difference between a narrow and wide transformation? Give 2 examples of each.
- Why is `groupByKey()` worse than `reduceByKey()` for large datasets?

**Interview Prep:**
- Q: "Explain the difference between `map` and `flatMap`."
  - *Expected:* `map` returns one output per input; `flatMap` returns zero or more (flattens nested lists) — e.g., splitting a sentence string into individual words
- Q: "Why is lazy evaluation important in Spark?"
  - *Expected:* Transformations build a DAG without executing; Spark optimizes the full plan before running (Catalyst optimizer) — avoids unnecessary computation
- Q: "How would you optimize a slow Spark job?"
  - *Expected:* Check for shuffles (groupBy, join), use broadcast joins for small tables, repartition on join key, cache intermediate DataFrames reused multiple times, use columnar Parquet format, avoid UDFs (use built-in functions)
- Q: "What is data skew in Spark and how do you fix it?"
  - *Expected:* One partition has far more data than others, causing one executor to run much longer. Fix: salt the skewed key, broadcast the smaller table, or repartition by a more granular key
- Q: "What is the Catalyst optimizer?"
  - *Expected:* Spark's query optimizer that applies logical and physical plan optimizations — predicate pushdown, constant folding, join reordering — before executing the DAG

**Tools to Use:**
- PySpark (local mode)
- Jupyter or IPython for experimentation
- Parquet format for efficient storage
- Spark documentation and Databricks tutorials

---

### Week 7: Cloud Data Platforms (AWS Focus)
**Duration:** 9-10 hours  
**Focus:** Cloud data warehousing and storage

**Topics:**
- AWS S3 basics (buckets, objects, partitioning)
- AWS RDS (relational database service)
- Amazon Redshift (data warehouse)
- AWS Glue (ETL service)
- AWS Lambda (serverless compute)
- Data catalog and metadata management
- Cost optimization
- Security (IAM, encryption)

**Deliverables:**

**AWS Hands-On Scenarios to Complete:**
1. **S3 Partitioned Data Lake:** Upload 3 months of CSV data to S3 partitioned as `s3://bucket/events/year=2024/month=01/day=01/`. Query it with AWS Athena and measure performance vs non-partitioned
2. **boto3 Scripting:** Write a Python script that: (a) lists all files in an S3 prefix modified in the last 24 hours, (b) downloads and processes them, (c) uploads the result back to a different prefix
3. **Glue Job Optimization:** Create a Glue ETL job that reads JSON from S3, converts to Parquet with snappy compression, and writes partitioned by date. Enable Glue Job Bookmarks to avoid reprocessing
4. **Redshift COPY:** Load a Parquet file from S3 into Redshift using the COPY command. Compare performance vs INSERT. Query `STL_LOAD_ERRORS` to debug a failed load
5. **Redshift Query Tuning:** Write a query that's slow. Check `STL_QUERY` and `SVL_QUERY_SUMMARY`. Add a sort key, run `VACUUM SORT ONLY`, and measure improvement

**Scenario-Based AWS Questions to Practice:**
- *"You have cold historical data in S3 that you occasionally join with hot data in Redshift. How do you query both without loading everything into Redshift?"* — Answer: Redshift Spectrum
- *"A Glue job is reprocessing already-processed files on every run. How do you fix it?"* — Answer: Enable Glue Job Bookmarks
- *"How do you load 1TB of data from S3 into Redshift as fast as possible?"* — Answer: Use COPY command with multiple manifest files, compress as GZIP or Parquet, split files to match Redshift slice count

**Interview Prep:**
- Q: "Design a data pipeline on AWS."
  - *Expected:* Ingestion (Kinesis/S3) → Cataloging (Glue Crawler) → ETL (Glue Job/Spark on EMR) → Warehouse (Redshift) → Analytics (Athena/QuickSight); mention IAM roles, encryption, cost optimization
- Q: "How would you partition data in S3 for efficient querying?"
  - *Expected:* Partition by the most common filter columns (e.g., `year/month/day` for time-series, `region/country` for geo). Enables partition pruning — Athena/Glue only scans relevant partitions
- Q: "When would you use Redshift vs RDS?"
  - *Expected:* Redshift for OLAP (analytics, large scans, aggregations, columnar storage); RDS for OLTP (transactional, row-level operations, frequent INSERTs/UPDATEs)
- Q: "What is Redshift Spectrum and when would you use it?"
  - *Expected:* Allows querying S3 data directly from Redshift without loading — useful for cold/archive data or very large datasets that don't need to live in the warehouse
- Q: "How do you handle schema evolution in AWS Glue?"
  - *Expected:* Use Schema Registry for Avro/Protobuf; or enable Crawler schema update behavior; or use Iceberg/Delta Lake format which supports schema evolution natively

**Tools to Use:**
- AWS Console
- boto3 (Python AWS SDK)
- AWS Glue console
- Redshift SQL
- AWS documentation

**Note:** Use free tier or minimal-cost setup to avoid unexpected bills

---

### Week 7b: Cloud Data Platforms (Azure Focus)
**Duration:** 9-10 hours  
**Focus:** Microsoft Azure data engineering services

**Topics:**
- Azure Data Lake Storage Gen2 (ADLS Gen2) — hierarchical namespace, partitioning
- Azure Synapse Analytics (unified analytics platform)
- Azure Data Factory (ADF) — ETL/ELT orchestration service
- Azure Databricks (managed Spark)
- Azure Event Hubs (streaming ingestion)
- Azure Stream Analytics (real-time query engine)
- Azure Active Directory (AAD) & RBAC security model
- Cost management and monitoring (Azure Monitor, Log Analytics)

**Deliverables:**

**Azure Hands-On Scenarios to Complete:**
1. **ADLS Gen2 Partitioned Lake:** Create a storage account with hierarchical namespace enabled. Upload CSV files partitioned as `container/raw/year=2024/month=01/day=01/`. Query with Azure Synapse Serverless SQL Pool using `OPENROWSET` — compare performance with and without partitioning
2. **Azure Data Factory Pipeline:** Build an ADF pipeline: (a) Copy Activity to pull data from HTTP source (public API) into ADLS Gen2 as raw JSON, (b) Data Flow Activity to transform and cast types, (c) Copy Activity to load to Azure Synapse dedicated SQL pool. Add a trigger for daily schedule
3. **Azure Databricks ETL:** Mount ADLS Gen2 to Databricks using Service Principal + OAuth. Read Parquet files, apply Bronze → Silver → Gold transformations, write back partitioned by date. Optimize with Delta Lake format: `df.write.format("delta").partitionBy("date").save(...)`  
4. **Synapse Analytics Query Tuning:** Load 10M rows into a Synapse Dedicated SQL Pool with different distribution strategies (`HASH`, `ROUND_ROBIN`, `REPLICATE`). Run the same analytical query on each and compare execution plans using `sys.dm_pdw_exec_requests`
5. **Azure Stream Analytics Job:** Create an Event Hub → Stream Analytics → Synapse/ADLS pipeline. Write a Stream Analytics query that counts events per `event_type` in a 5-minute tumbling window:
   ```sql
   SELECT event_type, COUNT(*) AS cnt, System.Timestamp AS window_end
   FROM eventhub TIMESTAMP BY event_time
   GROUP BY event_type, TumblingWindow(minute, 5)
   ```

**Azure vs AWS Service Mapping (Learn Both Sides):**
| Azure | AWS Equivalent | Purpose |
|-------|---------------|---------|
| ADLS Gen2 | S3 | Data lake storage |
| Azure Synapse | Redshift | Data warehouse |
| Azure Data Factory | AWS Glue | ETL orchestration |
| Azure Databricks | EMR + Glue | Spark processing |
| Event Hubs | Kinesis | Streaming ingestion |
| Stream Analytics | Kinesis Data Analytics | Real-time SQL on streams |
| Azure Monitor | CloudWatch | Logging & monitoring |
| AAD + RBAC | IAM | Identity & access |

**Scenario-Based Azure Questions to Practice:**
- *"You need to load 500GB of CSV files from ADLS Gen2 into Synapse dedicated pool daily. What's the fastest approach?"* — Use ADF Copy Activity with PolyBase/COPY INTO statement (parallel load); stage in Parquet format first for better compression; use `HASH` distribution on the most-queried join key
- *"Your ADF pipeline fails intermittently due to a flaky API. How do you make it resilient?"* — Enable retry policy on the Copy Activity (up to 3 retries, 30sec interval), add a Validation Activity before the copy to check if the source is available, use pipeline parameter for `runDate` to make it idempotent
- *"How do you control which team can access which data in ADLS Gen2?"* — Use Azure Data Lake ACLs at the directory level + AAD groups. Assign Storage Blob Data Reader/Contributor roles via RBAC. Use Azure Purview for data catalog and sensitivity labels on PII columns
- *"A Synapse query is scanning the entire table even though you filter by `customer_id`. Why?"* — Wrong distribution key. If the table is `ROUND_ROBIN` distributed and you filter by `customer_id`, all distributions are scanned. Fix: recreate table with `DISTRIBUTION = HASH(customer_id)`

**Interview Prep:**
- Q: "Explain the Azure data engineering stack. How does it compare to AWS?"
  - *Expected:* ADLS Gen2 (lake) + ADF (orchestration/ETL) + Databricks (Spark processing) + Synapse Analytics (warehouse + serverless queries) + Event Hubs (streaming). AWS equivalent: S3 + Glue + EMR + Redshift + Kinesis. Azure has tighter AAD integration; AWS has more mature serverless options (Athena vs Synapse Serverless)
- Q: "What is Azure Synapse Analytics and how does it differ from Azure SQL Database?"
  - *Expected:* Synapse is an analytics platform for OLAP workloads — massively parallel processing (MPP) across distributions, columnar storage, integrates with Spark and Serverless SQL. Azure SQL DB is a standard OLTP relational database — row-based, single node, optimized for transactional workloads
- Q: "What is the difference between Synapse Dedicated SQL Pool and Synapse Serverless SQL Pool?"
  - *Expected:* Dedicated: provisioned compute (DWUs), best for repeated heavy queries, you pay when paused too. Serverless: query-on-demand over ADLS files using `OPENROWSET`, pay per TB scanned — great for ad-hoc exploration without loading data
- Q: "How does Azure Data Factory compare to Apache Airflow?"
  - *Expected:* ADF: managed, GUI-driven, native Azure integration, limited custom logic, no Python-first authoring. Airflow: code-first (Python DAGs), more flexible for complex dependencies, requires self-hosting (or MWAA/Astronomer). Use ADF for straightforward Azure-native pipelines; Airflow when you need complex branching, custom operators, or multi-cloud
- Q: "How do you implement incremental loads in Azure Data Factory?"
  - *Expected:* Use a Lookup Activity to get `max(last_modified)` from a control table, pass it as a parameter to Copy Activity's source query (`WHERE updated_at > @{pipeline().parameters.watermark}`), update the control table watermark on success
- Q: "What is Delta Lake and why would you use it on Azure Databricks?"
  - *Expected:* Delta Lake adds ACID transactions, schema enforcement, time travel (versioning), and `MERGE` support on top of Parquet files in ADLS. Solves the problem of partial writes and schema drift in data lakes. Essential for SCD Type 2 implementations and idempotent pipelines on Databricks

**Tools to Use:**
- Azure Portal (free trial account)
- Azure Data Factory UI + JSON pipeline editor
- Azure Databricks Community Edition
- Azure Synapse Analytics workspace
- Azure CLI (`az` commands) for scripting
- Microsoft Learn (free Azure DE learning paths): https://learn.microsoft.com/en-us/training/

**Note:** Use Azure free trial ($200 credit for 30 days) or Azure for Students. Pause/delete resources after each exercise to avoid charges.

---

### Week 8: Data Warehousing & Dimensional Modeling
**Duration:** 8-9 hours  
**Focus:** Analytics database design

**Topics:**
- Star schema vs snowflake schema
- Fact tables (metrics) and dimension tables (attributes)
- Slowly Changing Dimensions (SCD Type 1, 2, 3)
- Conformed dimensions
- Grain of a fact table
- Fact table types (transactional, periodic, accumulating)
- Aggregate tables and materialized views

**Deliverables:**

**Dimensional Modeling Design Exercises:**
1. **Retail Star Schema:** Design fact table `fact_sales` with grain = one row per line item per transaction. Dimensions: `dim_date`, `dim_product`, `dim_store`, `dim_customer`. Include surrogate keys. Write queries for: daily revenue, top-10 products by store, customer repeat purchase rate
2. **SaaS Metrics Model:** Design `fact_subscriptions` (grain: one row per subscription per month-end). Dimensions: `dim_account`, `dim_plan`, `dim_date`. Derive MRR, churn rate, expansion revenue
3. **Airline Model:** `fact_flights` (grain: one flight segment). Dimensions: `dim_aircraft`, `dim_route`, `dim_date`, `dim_passenger`. Queries: on-time performance %, load factor by route, revenue per seat-mile

**SCD Type 2 Implementation Exercise:**
Given a `customers` table where addresses change, implement SCD Type 2:
```sql
-- dim_customer schema
Customer_SK (surrogate key), Customer_ID (natural key),
Name, Address, City, effective_start, effective_end, is_current
```
Write the MERGE/UPSERT logic that: inserts a new row on change, sets `effective_end` on old row, marks `is_current = FALSE` on old row

**Analytical SQL Queries to Write on Your Star Schema:**
1. Monthly revenue trend (last 12 months) — GROUP BY month with LAG() for MoM change
2. Top 5 products by revenue in each store — DENSE_RANK() window function
3. Customer cohort analysis: for users who signed up in Jan 2024, what % are still active each subsequent month?
4. Week-over-week sales growth % by product category

**Interview Prep:**
- Q: "Design a dimensional model for an airline."
  - *Expected:* `fact_flights` with grain=one flight per passenger-segment; dimensions: `dim_date`, `dim_route`, `dim_aircraft`, `dim_passenger`; mention surrogate keys, conformed dimensions (shared `dim_date` across fact tables)
- Q: "What is a slowly changing dimension? Explain Type 1, 2, and 3."
  - *Expected:* SCD tracks dimension attribute changes over time. Type 1: overwrite (no history). Type 2: new row per change with `effective_start/end + is_current` flag (full history, most common). Type 3: add `previous_value` column (limited history).
- Q: "Why use a star schema over normalized (3NF) tables for analytics?"
  - *Expected:* Fewer JOINs = faster analytical queries; intuitive for BI tools; columnar warehouses (Redshift, BigQuery) are optimized for wide table scans
- Q: "What is the grain of a fact table and why does it matter?"
  - *Expected:* The grain defines what one row represents. Wrong grain = wrong aggregations. E.g., if grain is per-order but you join with per-order-item data, you get row multiplication
- Q: "What is a degenerate dimension? Give an example."
  - *Expected:* A dimension attribute that has no dimension table — lives directly in the fact table. E.g., `order_number` in `fact_sales` — it's contextual but has no other attributes.

**Tools to Use:**
- PostgreSQL or Redshift
- Draw.io for schema diagrams
- dbt (data build tool) for transformation (optional preview)

---

## PHASE 3: ADVANCED & INTEGRATION (Weeks 9-11)

### Week 9: Workflow Orchestration & Scheduling
**Duration:** 9-10 hours  
**Focus:** Managing complex data pipelines

**Topics:**
- DAG (Directed Acyclic Graph) concepts
- Apache Airflow fundamentals
- Operators, tasks, and dependencies
- Scheduling and monitoring
- Error handling and alerting
- Backfill and retry logic
- Sensors and triggering

**Deliverables:**

**Airflow DAG Challenges to Build:**
1. **Simple ETL DAG:** `extract_from_postgres` → `transform_and_clean` → `load_to_s3` → `notify_slack`. Use `PostgresOperator`, `PythonOperator`, `S3Hook`. Set `retries=3, retry_delay=timedelta(minutes=5)`
2. **Idempotent Backfill DAG:** Parameterize with `{{ ds }}` (Airflow execution date). Ensure re-running for any past date produces same result without duplicates. Test by backfilling 7 days via CLI: `airflow dags backfill -s 2024-01-01 -e 2024-01-07 my_dag`
3. **Branching DAG:** Use `BranchPythonOperator` — if today is Monday, run `full_load_task`; otherwise run `incremental_load_task`. Downstream tasks should use `trigger_rule='none_failed_min_one_success'`
4. **Fan-out/Fan-in:** A `get_file_list` task yields a list of S3 files. Use `.expand()` (Dynamic Task Mapping) to process each file in parallel. A final `aggregate_results` task waits for all
5. **Rate-Limited API DAG:** Pull from an API that allows 100 requests/minute. Use Airflow Pools (concurrency=10) + `time.sleep()` inside PythonOperator. Handle 429 errors with exponential backoff

**DAG Design Questions to Answer in Writing:**
- Your DAG was accidentally paused for 10 days. `catchup=True` is set. What happens when you unpause it? How do you control this?
- How do you share state (e.g., a file path) between tasks in a DAG? (Answer: XCom push/pull — use sparingly for small values only)
- Task A and Task B run in parallel. Task C should only run if EITHER A or B succeeds (not both required). How do you configure this?
- How do you make Task B in DAG-2 wait for Task A in DAG-1 to complete? (Answer: `ExternalTaskSensor`)

**Interview Prep:**
- Q: "Design an Airflow pipeline for data ingestion from an external API."
  - *Expected:* `HttpSensor` (wait for API availability) → `PythonOperator` (fetch + validate) → `S3Hook` (upload raw) → `GlueJobOperator` (transform) → `RedshiftOperator` (load). Mention idempotency via `{{ ds }}` partitioning, retries, SLA alerts
- Q: "How would you handle task failures and retries in Airflow?"
  - *Expected:* Set `retries`, `retry_delay`, `retry_exponential_backoff=True`. Use `on_failure_callback` to send Slack/PagerDuty alerts. For critical pipelines, set `sla` and `email_on_sla_miss=True`
- Q: "Explain the difference between Sensors and Operators in Airflow."
  - *Expected:* Operators execute an action (run SQL, call API, run Python). Sensors wait for a condition to be true (S3 file exists, HTTP endpoint responds, external task done). Sensors should use `mode='reschedule'` to avoid holding worker slots
- Q: "What is the difference between `catchup=True` and `catchup=False`?"
  - *Expected:* `catchup=True`: Airflow runs all missed DAG runs since `start_date` when unpaused. `catchup=False`: Only runs the most recent interval. Use False for real-time pipelines; True only when backfilling is intentional and idempotency is guaranteed
- Q: "How do you avoid top-level code issues in DAG files?"
  - *Expected:* Never put DB connections, API calls, or heavy imports at the DAG file's top level — the Scheduler parses every DAG file every `min_file_process_interval` seconds. Use `with DAG(...)` context manager and initialize connections inside task callables

**Tools to Use:**
- Apache Airflow (Docker recommended)
- Python for DAG definition
- PostgreSQL as metadata store
- Airflow UI for monitoring

---

### Week 10: Real-Time Data & Stream Processing
**Duration:** 9-10 hours  
**Focus:** Event-driven data systems

**Topics:**
- Message queues (Kafka, RabbitMQ, AWS Kinesis)
- Streaming vs batch processing
- Windowing and aggregations
- Exactly-once vs at-least-once semantics
- Stateful processing
- Stream processing frameworks (Spark Streaming, Kafka Streams)
- Use cases (real-time analytics, anomaly detection, monitoring)

**Deliverables:**

**Kafka Hands-On Exercises:**
1. **Producer/Consumer:** Write a Python Kafka producer that publishes 1000 fake user events (`{user_id, event_type, timestamp}`) to a topic. Write a consumer that reads, validates, and prints events
2. **Consumer Group Lag Monitoring:** Run two consumers in the same consumer group. Generate load. Check lag with `kafka-consumer-groups.sh --describe`. Add a 3rd consumer and observe partition rebalancing
3. **Dead Letter Queue (DLQ):** Modify your consumer so that malformed messages (missing required fields) are published to a `events-dlq` topic instead of crashing the consumer
4. **Windowed Aggregation:** Using PySpark Structured Streaming, read from a Kafka topic and compute: count of events per `event_type` in 5-minute tumbling windows. Write results to PostgreSQL
5. **Exactly-Once Setup:** Configure Kafka producer with `enable.idempotence=True` and `acks=all`. Explain what `min.insync.replicas=2` does and when to use it

**Scenario Questions to Practice Explaining:**
- *"Your real-time pipeline has significant consumer lag during peak hours. Walk me through diagnosing and fixing it."* — Check consumer group lag, check processing time per message, add consumers (up to partition count), optimize processing logic, consider increasing partitions
- *"A malformed message is crashing your consumer repeatedly (poison pill). How do you handle it without stopping the pipeline?"* — Wrap processing in try/except, publish bad messages to DLQ topic, commit offset to skip, alert team
- *"You need to join two Kafka streams: user signups and user purchases. How do you do this?"* — Both topics must be co-partitioned on `user_id`; use KTable-KStream join in Kafka Streams or stream-stream join with watermarks in Spark Structured Streaming

**Interview Prep:**
- Q: "Design a real-time data pipeline for user events (100k events/sec)."
  - *Expected:* Event sources → Kafka (partitioned by `user_id`) → Spark Structured Streaming (validate, deduplicate, aggregate) → write to data warehouse (Redshift/BigQuery) + Redis for low-latency lookups + S3 for raw archive. Mention DLQ, monitoring, exactly-once
- Q: "Explain exactly-once semantics in stream processing."
  - *Expected:* At-most-once (messages can be lost), at-least-once (duplicates possible on failure/retry), exactly-once (each message processed exactly once). Achieved in Kafka Streams via transactional API; in Spark via checkpointing + idempotent sinks
- Q: "How would you detect anomalies in a real-time stream?"
  - *Expected:* Statistical thresholds (z-score, rolling mean ± 3σ), sliding window aggregations with `LAG()` to detect sudden spikes, ML models (Isolation Forest) applied per micro-batch, alert via Kafka topic → PagerDuty
- Q: "What is watermarking in stream processing?"
  - *Expected:* A mechanism to handle late-arriving data. You define max lateness (e.g., 10 minutes). Events with timestamp more than 10 mins behind the current watermark are dropped. Allows closing windows and emitting results without waiting forever
- Q: "What is the difference between Kafka Streams and Spark Structured Streaming?"
  - *Expected:* Kafka Streams: lightweight Java library, stateful processing, runs in your app (no separate cluster). Spark Structured Streaming: distributed cluster-based, better for complex batch+stream unified processing, larger scale

**Tools to Use:**
- Apache Kafka (Docker)
- PySpark Structured Streaming
- Python clients (confluent-kafka, pykafka)
- Monitoring tools (Kafka UI, Grafana)

---

### Week 11: System Design & Advanced Architectures
**Duration:** 10-12 hours  
**Focus:** End-to-end data system design

**Topics:**
- Data pipeline design principles
- Scalability, reliability, maintainability
- Handling late data and out-of-order events
- Data quality frameworks
- Metadata management
- Cost optimization
- Case studies: Data lake, data warehouse, lakehouse (Delta Lake, Apache Iceberg)
- Modern stacks (dbt + Snowflake, Spark + Delta Lake)

**Deliverables:**

**System Design Exercise 1: Design a Real-Time Analytics Platform**

*Scenario:* A social media company processes 500k user events/sec (clicks, views, likes). Business needs: real-time dashboard (< 2sec latency), historical trend analysis (2 years), data quality monitoring.

*Structure your design around these steps:*
1. **Clarify:** What's the event schema? Who are the consumers (dashboards, ML, data science)? SLA for freshness?
2. **Estimate:** 500k events/sec × 1KB each = 500MB/sec = ~43TB/day raw. 2 years = ~31PB total \u2192 need tiered storage
3. **Design the layers:** Ingestion (Kafka, 50 partitions by `user_id`) \u2192 Stream Processing (Spark Structured Streaming: validate, deduplicate on `event_id`) \u2192 Hot store (ClickHouse/Druid for real-time dashboards) + Cold store (S3 Parquet, partitioned by date, queried via Athena/Redshift Spectrum)
4. **Data quality:** Row count checks per partition, schema validation via Schema Registry, SLA alerts if lag > 30sec
5. **Trade-offs:** Lambda (separate batch + stream) vs Kappa (unified stream) architecture

**System Design Exercise 2: Design a Data Lake for a Retail Company**

*Scenario:* 500 stores across 20 countries. Multiple teams: analytics (SQL), ML (Python/Spark), operations (low-latency). Data: sales transactions, inventory, customer profiles. Requirements: schema evolution, data governance, incremental processing.

*Structure your answer:*
1. **Zones:** Bronze (raw, immutable, S3) \u2192 Silver (cleaned, typed, deduplicated, Delta Lake) \u2192 Gold (aggregated, domain-specific, Redshift/Snowflake)
2. **Schema evolution:** Use Delta Lake or Apache Iceberg — both support column additions without full rewrites
3. **Governance:** Column-level access control (AWS Lake Formation), PII tagging (`customer_email` masked), data catalog (AWS Glue Catalog or Apache Atlas)
4. **Incremental processing:** CDC from store POS systems via Debezium \u2192 Kafka; or file-based: new files detected via S3 event notifications \u2192 Glue Job Bookmarks
5. **Multi-team access:** Analytics team \u2192 Redshift (SQL); ML team \u2192 S3 + SageMaker; Operations \u2192 DynamoDB cache refreshed by stream

**System Design Exercise 3: Design a Data Platform for a Social Media Company**

*Prompt (time yourself to 45 minutes):*
"Design a data platform for a social media company with 1B users. The platform must support: (1) real-time feed ranking, (2) weekly user engagement reports, (3) advertiser campaign analytics, (4) ML training data pipelines."

*Key points to cover:* separate serving layers per use case, event bus (Kafka), feature store for ML, data warehouse for reporting, cost-sharing via logical data zones

**Interview Prep:**
- Q: "Design a data platform for a social media company."
  - *Framework:* Clarify \u2192 Estimate scale \u2192 Design layers (ingest/store/process/serve) \u2192 Pick tech with justification \u2192 Discuss failure modes + cost
  - *Expected:* Kafka for event ingestion, Spark for batch + stream processing, S3 as data lake (Bronze/Silver/Gold), Redshift/Snowflake for analytical queries, Redis/DynamoDB for low-latency serving, Airflow for orchestration
- Q: "How would you handle schema changes in a streaming pipeline?"
  - *Expected:* Use Schema Registry (Confluent/AWS Glue) for Avro/Protobuf with backward compatibility mode. For Parquet/Delta, use schema evolution flags. For breaking changes: version the topic (`events_v2`), run dual-write during migration, decommission old topic after consumers migrated
- Q: "Explain the trade-offs between a data lake and a data warehouse."
  - *Expected:* Data lake: raw/unstructured, cheap storage (S3), schema-on-read, flexible (ELT), but slower queries without optimization. Data warehouse: structured, schema-on-write, fast analytical queries, but expensive and rigid. Lakehouse (Delta/Iceberg) combines both: ACID on S3, fast queries, schema enforcement.
- Q: "What is the Lambda architecture? What is the Kappa architecture? Which do you prefer and why?"
  - *Expected:* Lambda: separate batch layer (accurate, slow) + speed layer (fast, approximate), merged at serving layer \u2014 complex to maintain two codebases. Kappa: reprocess everything via a single stream layer \u2014 simpler, but stream processing must handle historical backfills. Prefer Kappa for simplicity when stream framework can handle replay.
- Q: "You discover a data quality issue: 15% of orders are missing `customer_id` for the past 3 hours. Walk me through your response."
  - *Expected:* Stop/pause downstream jobs, quarantine affected records, check upstream source (API/DB change?), compare with yesterday's data, notify stakeholders, backfill once root cause fixed, add automated alert for `NULL rate > 5%` in future

**Tools to Use:**
- Miro or Lucidchart for architecture diagrams
- AWS/GCP cost calculators
- Data architecture patterns documentation

---

## PHASE 4: CAPSTONE & INTERVIEW PREP (Week 12)

### Week 12: Capstone Project & Final Preparation
**Duration:** 12-15 hours  
**Focus:** Integrate all learning into a portfolio-ready project

**Capstone Project: End-to-End Data Platform**

**Project Scope:** Build a complete data engineering solution demonstrating all skills

**Architecture:**
```
Raw Data (CSV/API) 
    ↓
Data Ingestion (Python/Spark)
    ↓
Data Lake (S3 + Partitioning)
    ↓
Transformation (Spark/dbt)
    ↓
Data Warehouse (Redshift/Postgres)
    ↓
Analytics & Dashboards
    ↓
Orchestration (Airflow DAG)
```

**Requirements:**
1. **Data Source:** Multiple sources (CSV files, API, database)
2. **Ingestion:** Robust data loading with validation and error handling
3. **Storage:** Proper partitioning and file format (Parquet)
4. **Transformation:** Multi-stage ETL with business logic
5. **Warehouse:** Dimensional model (star schema)
6. **Orchestration:** Airflow DAG scheduling daily runs
7. **Monitoring:** Data quality checks, pipeline alerts, logging
8. **Documentation:** Schema docs, data lineage, architecture diagrams
9. **Testing:** Unit tests for transformations

**Example Domain Options:**
- **E-Commerce Analytics:** Orders, customers, products, reviews
- **SaaS Metrics:** User signups, subscriptions, usage, churn
- **Social Media Analytics:** Posts, interactions, user growth
- **Stock Market Analytics:** Price data, volume, sentiment
- **Weather Analytics:** Historical weather data, forecasting, trends

**Deliverables:**
- [ ] GitHub repo with complete code (organized, documented)
- [ ] Architecture diagram (high-level data flow)
- [ ] README with setup instructions
- [ ] Data model documentation (ERD + descriptions)
- [ ] Airflow DAG visualization and explanation
- [ ] Sample queries/analytics output
- [ ] List of improvements and scaling plans
- [ ] 2-3 minute demo video (optional but powerful)

**Interview Prep Intensive:**

**Technical Deep Dives — Specific LeetCode Problems for Final Review:**

*SQL (aim to solve these without hints):*
- [185. Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/) — DENSE_RANK window
- [180. Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers/) — self-join or LAG
- [1321. Restaurant Growth](https://leetcode.com/problems/restaurant-growth/) — 7-day rolling avg with window
- [1341. Movie Rating](https://leetcode.com/problems/movie-rating/) — UNION of two aggregations
- [601. Human Traffic of Stadium](https://leetcode.com/problems/human-traffic-of-stadium/) — consecutive rows with count ≥ 100
- [615. Average Salary: Departments vs Company](https://leetcode.com/problems/average-salary-departments-vs-company/) — compare against overall avg
- [1907. Count Salary Categories](https://leetcode.com/problems/count-salary-categories/) — UNION with CASE WHEN bucketing
- [1204. Last Person to Fit in the Bus](https://leetcode.com/problems/last-person-to-fit-in-the-bus/) — running sum with window

*Python / Algorithms (DE-relevant patterns):*
- [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) — scheduling, time-range merging
- [57. Insert Interval](https://leetcode.com/problems/insert-interval/) — dynamic interval insertion
- [207. Course Schedule](https://leetcode.com/problems/course-schedule/) — topological sort / DAG cycles (Airflow!)
- [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) — return the execution order
- [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) — hash set O(n)
- [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) — heap or bucket sort
- [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) — sliding window (stream processing analog)
- [23. Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) — heap merge (merging data streams)

*System Design Prompts to Practice (45 min each):*
1. Design a URL shortener with analytics (high-write, high-read, daily click counts)
2. Design a ride-sharing data platform (driver locations, trip events, surge pricing analytics)
3. Design a data pipeline for financial transactions (exactly-once, fraud detection, regulatory reporting)
4. Design a recommendations system data pipeline (user events → feature store → model training → serving)
5. Design a data observability platform (monitor pipeline freshness, quality, volume anomalies)

**Behavioral Prep — STAR Format Questions:**
- "Tell me about a time you debugged a complex data issue."
  - *Structure:* What was the pipeline? What went wrong? How did you isolate the cause (add logging, check row counts, diff source vs target)? What was the fix? What monitoring did you add to prevent recurrence?
- "Describe a time you optimized a slow data pipeline."
  - *Structure:* What was the baseline performance? What did you diagnose (profiling, EXPLAIN PLAN, Spark UI)? What optimization did you apply (indexes, partitioning, broadcast join, caching)? What was the improvement (X% faster)?
- "Tell me about a time you worked with stakeholders on data requirements."
  - *Structure:* Who were the stakeholders (product, analytics, finance)? What was unclear? How did you clarify (document assumptions, define metric formulas)? How did you validate the output matched their expectation?
- "Describe a trade-off decision you made in a data engineering project."
  - *Structure:* What were the options (e.g., real-time vs batch, star schema vs normalized)? What factors did you weigh (cost, latency, complexity, team skill)? What did you choose and why? What would you do differently?

**Final Review Checklist:**
- [ ] Can explain SQL window functions with examples (RANK, LAG, SUM OVER)
- [ ] Can design a normalized and dimensional database from scratch in 20 mins
- [ ] Can write production-quality Python (error handling, logging, retry decorator, unit tests)
- [ ] Can optimize Spark jobs (identify shuffles, use broadcast, repartition, cache)
- [ ] Can architect a complete data pipeline (ingest → store → transform → serve → monitor)
- [ ] Can explain trade-offs (batch vs real-time, lake vs warehouse, star vs snowflake, ETL vs ELT)
- [ ] Have a polished portfolio with 3+ projects on GitHub with READMEs
- [ ] Can answer 30+ common DE interview questions with *Expected* answers
- [ ] Can solve a system design problem in 45 minutes using Clarify → Estimate → Design → Trade-offs framework
- [ ] Completed LeetCode SQL 50 plan and 30 Days of Pandas

---

## Weekly Study Schedule Template

**Daily Commitment:** 1.5-2.5 hours (9-15 hours/week)

```
Monday:      2 hours - Review concepts, start new topic
Tuesday:     2 hours - Deep dive + coding practice
Wednesday:   2 hours - Problem solving + optimization
Thursday:    1.5 hours - Consolidate learning, write notes
Friday:      2.5 hours - Project work or advanced problems
Saturday:    2 hours - Review weak areas, interview prep
Sunday:      1.5 hours - Plan next week, update progress
```

---

## Progress Tracking

Track your progress in Notion with these metrics:

| Week | Topic | Hours | Status | Interview Qs | Projects |
|------|-------|-------|--------|--------------|----------|
| 1 | SQL | 8/8 | ✅ Complete | 3/3 | - |
| 2 | Python | 8/8 | ✅ Complete | 3/3 | CSV Parser |
| 3 | Data Modeling | 9/9 | ✅ Complete | 3/3 | ER Diagram |
| 4 | Foundational Project | 10/10 | 🔄 In Progress | 10/10 | E-Com Pipeline |
| ... | ... | ... | ... | ... | ... |

---

## Resource Recommendations by Topic

### SQL
- LeetCode SQL (500+ problems)
- SQLZoo (interactive tutorials)
- Mode Analytics SQL Tutorial
- Stratascratch (real company problems)

### Python
- LeetCode Python
- Real Python tutorials
- Automate the Boring Stuff (free book)
- DataCamp (Python for data science)

### Data Modeling
- Database Design Manual (C.J. Date)
- Fundamentals of Dimensional Modeling (Ralph Kimball)
- YouTube: Lucidchart ER diagrams

### Spark
- Databricks Academy (free)
- "Learning Spark" book
- Official Spark documentation
- YouTube: Frank Kane's Spark courses

### AWS
- AWS Skill Builder (free tier)
- Stephane Maarek's AWS courses (Udemy)
- Hands-on labs on A Cloud Guru

### Airflow
- Official Airflow documentation
- Marc Lamberti's Udemy course
- YouTube tutorials

### System Design
- "Designing Data-Intensive Applications" by Martin Kleppmann
- ByteByteGo (Alex Xu's YouTube channel)
- System Design Interview (AlgoExpert)
- Educative.io courses

### Interview Prep
- LeetCode
- Stratascratch
- Interview.io (mock interviews)
- Pramp (peer mock interviews)

---

## Tips for Success

1. **Code Every Day:** 80% of learning is hands-on coding
2. **Build Projects:** Theoretical knowledge + practical work = jobs
3. **Read Code:** Study open-source data engineering projects (Airflow, dbt, etc.)
4. **Document Everything:** Write blog posts or Notion pages explaining concepts—forces clarity
5. **Join Communities:** r/dataengineering, Slack communities, Meetups
6. **Do Mock Interviews:** Start at week 8, do 1-2 per week
7. **Focus on Weaknesses:** Identify weak areas weekly and deep-dive
8. **Stay Current:** Follow data engineering blogs and podcasts
9. **Network:** Connect with DE professionals on LinkedIn, attend meetups
10. **Rest:** Don't burn out—consistency beats intensity

---

## Post-12-Week Continuation

After 12 weeks, you should be interview-ready. Next steps:

- **Month 4:** Apply to jobs, do interviews, refine weak areas based on feedback
- **Month 5-6:** Continue applying and interviewing; deep-dive into target company stacks
- **Ongoing:** Stay updated with new tools (dbt, Iceberg, etc.) and deepen expertise in specializations (real-time, ML ops, etc.)

---

**Remember:** The goal isn't to learn everything—it's to build a strong foundation and demonstrate the ability to solve real data engineering problems. Focus on depth in a few areas rather than breadth across everything.

Good luck! 🚀
