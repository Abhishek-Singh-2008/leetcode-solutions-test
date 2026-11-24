# Valid Anagram

**Difficulty:** 🟢 **Easy**  
**LeetCode Link:** [Valid Anagram](https://leetcode.com/problems/valid-anagram/)

---

## Solutions

### 🐍 Python3 — Approach 2 (`solution_2.py`)

- **Synchronized:** November 24, 2026
- **Language:** `Python3`
- **Source File:** [`solution_2.py`](solution_2.py)

#### 💡 Approach & Intuition

> The solution checks if two strings are anagrams by sorting both strings and comparing the resulting sorted character sequences for equality.

#### ⏱️ Complexity Analysis

- **Time Complexity:** `O(N log N)` — *Sorting two strings of combined length N takes O(N log N) time.*
- **Space Complexity:** `O(N)` — *The sorting algorithm requires O(N) auxiliary space to store the character lists in memory.*

---

### 🐍 Python3 (`solution.py`)

- **Synchronized:** November 24, 2026
- **Language:** `Python3`
- **Source File:** [`solution.py`](solution.py)

#### 💡 Approach & Intuition

> The algorithm uses a recursive depth-first search approach to validate the binary search tree by maintaining a valid range (low, high) for each node's value.

#### ⏱️ Complexity Analysis

- **Time Complexity:** `O(N)` — *Every node in the binary tree is visited exactly once.*
- **Space Complexity:** `O(H)` — *The auxiliary space is determined by the recursion stack, which can grow up to the height H of the tree.*
