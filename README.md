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