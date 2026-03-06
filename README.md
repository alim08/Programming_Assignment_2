# COP4533_Programming_Assignment2

## Team Members
* **Justin Oh** (78478358)
* **Adam Lim** (23149660)

## Project Overview


This project implements and compares three different cache eviction policies on a sequence of page requests, including:
* **FIFO (First-In, First-Out):** Evicts the item that has been in the cache the longest.
* **LRU (Least Recently Used):** Evicts the item whose most recent access time is the oldest.
* **OPTFF (Belady's Farthest-in-Future):** The optimal offline algorithm that evicts the item whose next request occurs farthest in the future.

## Directory Structure
* `src/cache_sim.py`: The core simulator containing the `CacheSimulator` class and the three eviction algorithms.
* `generate_tests.py`: A utility script to generate nontrivial random and edge-case input sequences.
* `data/`: Contains the provided `example.in` and expected `example.out`.
* `tests/`: Contains the generated test files (`file1.in`, `file2.in`, `file3.in`) used for empirical analysis.

## Setup & Dependencies
* The project is written in **Python 3**.
* No compilation is required.
* **Standard Libraries used:** `sys`, `collections`, `random`, `os`.

## How to Run

The simulator reads an input file from standard arguments and outputs the total number of cache misses for each policy to `stdout`.

**Command:**
```bash
python3 src/cache_sim.py <input_file>
```

## Written Component

### Question 1: Empirical Comparison

| Input File | k | m | FIFO | LRU | OPTFF |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `tests/file1.in` (High Locality) | 5 | 60 | 31 | 28 | 20 |
| `tests/file2.in` (Uniform Random) | 10 | 100 | 62 | 66 | 40 |
| `tests/file3.in` (Looping Sequence) | 3 | 75 | 75 | 75 | 27 |

**Trend Analysis & Comments:**
* **Does OPTFF have the fewest misses?** Yes. OPTFF consistently yields the fewest misses across all test cases because it utilizes perfect offline knowledge of future requests to make optimal eviction choices.
* **How does FIFO compare to LRU?** LRU performs better than FIFO on sequences with high temporal locality (`file1.in`). However, on purely random sequences (`file2.in`), LRU offers no distinct advantage. On the looping worst-case sequence (`file3.in`), both fail completely with a 100% miss rate.

### Question 2: Bad Sequence for LRU or FIFO
For `k = 3`, there exists a sequence where OPTFF incurs strictly fewer misses than LRU.

* **The Sequence:** `1 2 3 4 1 2 3 4 1 2 3 4 ...` (Repeating 1 - 4 for 75 requests, as simulated in `file3.in`).
* **LRU Misses:** 75 misses
* **OPTFF Misses:** 27 misses
* **Reasoning:** In LRU, when the working set size (4 distinct items) is exactly one larger than the cache capacity (3), every single request evicts the exact item that will be requested next. This results in a 100% miss rate. OPTFF avoids this by evicting the item needed furthest in the future.

### Question 3: Prove OPTFF is Optimal
We prove Belady’s Farthest-in-Future (OPTFF) is optimal using an exchange argument.

Let S be a request sequence, and let A be any optimal offline algorithm. Assume A matches OPTFF for the first i-1 steps but diverges at step i. At step i, a miss occurs. OPTFF evicts item X (the one needed farthest in the future), while A evicts item Y. 

We can construct a new schedule A' that mimics A, except at step i, A' evicts X instead of Y. Because X is requested further in the future than Y, A' will have Y in the cache when it is requested earlier, saving a miss compared to A. When X is finally requested, A' might incur a miss. Overall, the total misses of A' will be less than or equal to A. By repeating this exchange at every point of divergence, we transform A into OPTFF without ever increasing total misses.


## Assumptions

### 1. Input Format
* **Structure:** We assume the input strictly follows the assignment specification:
    * **Line 1:** Two integers `k` (capacity) and `m` (requests).
    * **Line 2:** A sequence of `m` integer IDs separated by spaces.

### 2. Output Format
* The program outputs exactly three lines to `stdout` matching the format: `<POLICY> : <number_of_misses>`.

### 3. Dependencies
* **Python Version:** The code assumes a standard **Python 3** environment.
* **Libraries:** Relies solely on `sys` and `collections`.
