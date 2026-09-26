# Find Center of Star Graph

**Difficulty:** Easy

## Problem

[LeetCode — Find Center of Star Graph](https://leetcode.com/problems/find-center-of-star-graph/)

## Solutions

### 🐍 Python3 — Approach 2 (`solution_2.py`)

- **Synchronized:** September 26, 2026

#### Approach & Intuition

> The center of a star graph appears in every edge, so it must be one of the two vertices in the first edge. Check whether the first vertex of the first edge is present in the second edge; if so, it is the center, otherwise the other vertex is.

#### Complexity

- **Time Complexity:** `O(1)` — Only a constant number of comparisons between the first two edges are performed, independent of the number of edges.
- **Space Complexity:** `O(1)` — No additional data structures or recursion are used, so auxiliary space is constant.

---

### 🐍 Python3 (`solution.py`)

- **Synchronized:** September 26, 2026

#

---

### Complexity

> ⚠️ *Complexity analysis unavailable (Analysis timed out (connectivity / latency issue)).*

---

---

### ☕ Java (`solution.java`)

- **Synchronized:** September 26, 2026

#

---

---

### Approach & Intuition

> Count the degree of every vertex by iterating over all edges; in a star graph, the center is the only vertex with degree n-1.

#

---

---

### Complexity

- **Time Complexity:** `O(N)` — The algorithm iterates through N-1 edges and then through N vertices, giving O(N) total time.
- **Space Complexity:** `O(N)` — An auxiliary degree array of size N+1 is used, requiring O(N) extra space.
