# Find Center of Star Graph

**Difficulty:** Easy

**Language:** Python3

## Problem

https://leetcode.com/problems/find-center-of-star-graph/

## Solution

Automatically synchronized from LeetCode on September 26, 2026.

## Approach & Intuition

> The center of a star graph must be the common node shared by every edge, so it suffices to inspect only the first two edges: whichever node from the first edge also appears in the second edge is the center.

## Complexity

- **Time Complexity:** `O(1)` — The algorithm performs a single membership check against a fixed 2-element list (edges[1]), independent of the total number of edges.
- **Space Complexity:** `O(1)` — Only a constant number of comparisons are used with no auxiliary data structures or recursion.
