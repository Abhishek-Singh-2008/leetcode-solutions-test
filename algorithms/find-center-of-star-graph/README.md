# Find Center of Star Graph

**Difficulty:** Easy

**Language:** Python3

## Problem

https://leetcode.com/problems/find-center-of-star-graph/

## Solution

Automatically synchronized from LeetCode on September 26, 2026.

## Approach & Intuition

> Since the center of a star graph appears in every edge, it must be one of the two nodes in the first edge; check which of those two nodes also appears in the second edge and return it.

## Complexity

- **Time Complexity:** `O(1)` — The solution performs a single membership check against a fixed 2-element list, regardless of the number of edges.
- **Space Complexity:** `O(1)` — Only constant extra space is used, with no additional data structures or recursion.
