# Find Center of Star Graph

**Difficulty:** Easy

## Problem

[LeetCode — Find Center of Star Graph](https://leetcode.com/problems/find-center-of-star-graph/)

## Solutions

### ☕ Java (`solution.java`)

- **Synchronized:** September 28, 2026

#### Approach & Intuition

> Count the degree of every node by iterating over all edges, then return the unique node whose degree equals n-1, since the center of a star graph is connected to all other n-1 nodes.

#### Complexity

- **Time Complexity:** `O(N)` — The algorithm makes two linear passes: one over the E = N-1 edges to build degree counts and one over the N nodes to find the degree n-1 node.
- **Space Complexity:** `O(N)` — An auxiliary degree array of size N+1 is allocated to store each node's edge count.

---

### 🐍 Python3 (`solution.py`)

- **Synchronized:** September 28, 2026

#

---

### Approach & Intuition

> In a star graph, the center must appear in every edge, so compare the two endpoints of the first edge against the second edge and return the shared vertex.

#

---

### Complexity

- **Time Complexity:** `O(1)` — The algorithm performs a constant number of comparisons and membership checks on at most two edges.
- **Space Complexity:** `O(1)` — It uses only a constant amount of auxiliary space for the conditional expression.
