# Find Center of Star Graph

**Difficulty:** Easy

## Problem

[LeetCode — Find Center of Star Graph](https://leetcode.com/problems/find-center-of-star-graph/)

## Solutions

### ☕ Java (`solution.java`)

- **Synchronized:** September 26, 2026

#### Approach & Intuition

> Count the degree of every vertex by iterating over all edges; in a star graph, the center is the only vertex with degree n-1.

#### Complexity

- **Time Complexity:** `O(N)` — The algorithm iterates through N-1 edges and then through N vertices, giving O(N) total time.
- **Space Complexity:** `O(N)` — An auxiliary degree array of size N+1 is used, requiring O(N) extra space.
