# Find Center of Star Graph

**Difficulty:** Easy

## Problem

[LeetCode — Find Center of Star Graph](https://leetcode.com/problems/find-center-of-star-graph/)

## Solutions

### 🐍 Python3 (`solution.py`)

- **Synchronized:** September 28, 2026

#### Approach & Intuition

> In a star graph, the center must appear in every edge, so compare the two endpoints of the first edge against the second edge and return the shared vertex.

#### Complexity

- **Time Complexity:** `O(1)` — The algorithm performs a constant number of comparisons and membership checks on at most two edges.
- **Space Complexity:** `O(1)` — It uses only a constant amount of auxiliary space for the conditional expression.
