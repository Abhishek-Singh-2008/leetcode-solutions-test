# Valid Anagram

**Difficulty:** 🟢 **Easy**  
**LeetCode Link:** [Valid Anagram](https://leetcode.com/problems/valid-anagram/)

---

## Solutions

### 🐍 Python3 (`solution.py`)

- **Synchronized:** November 24, 2026
- **Language:** `Python3`
- **Source File:** [`solution.py`](solution.py)

#### 💡 Approach & Intuition

> The algorithm uses a recursive depth-first search approach to validate the binary search tree by maintaining a valid range (low, high) for each node's value.

#### ⏱️ Complexity Analysis

- **Time Complexity:** `O(N)` — *Every node in the binary tree is visited exactly once.*
- **Space Complexity:** `O(H)` — *The auxiliary space is determined by the recursion stack, which can grow up to the height H of the tree.*
