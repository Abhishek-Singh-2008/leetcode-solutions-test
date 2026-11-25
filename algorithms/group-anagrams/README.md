# Group Anagrams

**Difficulty:** 🟡 **Medium**  
**LeetCode Link:** [Group Anagrams](https://leetcode.com/problems/group-anagrams/)

---

## Solutions

### 🐍 Python3 (`solution.py`)

- **Synchronized:** November 25, 2026
- **Language:** `Python3`
- **Source File:** [`solution.py`](solution.py)

#### 💡 Approach & Intuition

> The solution groups anagrams by sorting each string to create a canonical key and appending the original string to a hash map with that key.

#### ⏱️ Complexity Analysis

- **Time Complexity:** `O(N * K log K)` — *For each of the N strings of maximum length K, we sort its characters which takes O(K log K) time.*
- **Space Complexity:** `O(N * K)` — *The hash map stores all N strings of maximum length K across the keys and grouped lists.*
