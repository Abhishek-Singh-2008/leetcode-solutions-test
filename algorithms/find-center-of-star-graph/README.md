# Find Center of Star Graph

**Difficulty:** Easy

## Problem

[LeetCode — Find Center of Star Graph](https://leetcode.com/problems/find-center-of-star-graph/)

## Solutions

### 🐍 Python3 — Approach 3 (`solution_3.py`)

- **Synchronized:** September 28, 2026

#### Approach & Intuition

> Count each node's degree while traversing the edges, then return the node whose degree equals the number of edges, which is the center of a star graph.

#### Complexity

- **Time Complexity:** `O(V + E)` — The solution processes all E edges to build the degree counts and then checks at most V nodes.
- **Space Complexity:** `O(V)` — The degree dictionary stores one entry for each of the V nodes.

---

### 🐍 Python3 — Approach 2 (`solution_2.py`)

- **Synchronized:** September 28, 2026

#

---

### Approach & Intuition

> The center of a star graph is the only node present in every edge, so it must be the single node shared by any two edges. The solution computes the set intersection of the first two edges and returns that one common node.

#

---

### Complexity

- **Time Complexity:** `O(1)` — Only the first two edges are examined, and each edge contains exactly 2 nodes, so building the sets and intersecting them takes constant time regardless of input size.
- **Space Complexity:** `O(1)` — Only two sets of constant size 2 (one per edge) are created, so auxiliary space is constant.

---

---

### ☕ Java (`solution.java`)

- **Synchronized:** September 28, 2026

#

---

---

### Approach & Intuition

> Count the degree of every node by iterating over all edges, then return the unique node whose degree equals n-1, since the center of a star graph is connected to all other n-1 nodes.

#

---

---

### Complexity

- **Time Complexity:** `O(N)` — The algorithm makes two linear passes: one over the E = N-1 edges to build degree counts and one over the N nodes to find the degree n-1 node.
- **Space Complexity:** `O(N)` — An auxiliary degree array of size N+1 is allocated to store each node's edge count.

---

---

---

### 🐍 Python3 (`solution.py`)

- **Synchronized:** September 28, 2026

#

---

---

---

### Approach & Intuition

> In a star graph, the center must appear in every edge, so compare the two endpoints of the first edge against the second edge and return the shared vertex.

#

---

---

---

### Complexity

- **Time Complexity:** `O(1)` — The algorithm performs a constant number of comparisons and membership checks on at most two edges.
- **Space Complexity:** `O(1)` — It uses only a constant amount of auxiliary space for the conditional expression.
