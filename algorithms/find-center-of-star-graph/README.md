# Find Center of Star Graph

**Difficulty:** Easy

**Language:** Python3

## Problem

https://leetcode.com/problems/find-center-of-star-graph/

## Solution

Automatically synchronized from LeetCode on September 26, 2026.

## Approach & Intuition

> The center of a star graph is the only vertex that belongs to every edge. By checking the two endpoints of the first edge against the endpoints of the second edge, the common vertex is returned directly.

## Complexity

- **Time Complexity:** `O(1)` — The algorithm only inspects the first two edges and performs a constant number of membership checks, independent of the graph size.
- **Space Complexity:** `O(1)` — Only a few scalar variables are used, with no extra data structures or recursion stack, so auxiliary space is constant.
