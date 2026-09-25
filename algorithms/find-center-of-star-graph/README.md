# Find Center of Star Graph

**Difficulty:** Easy

**Language:** Python3

## Problem

https://leetcode.com/problems/find-center-of-star-graph/

## Solution

Automatically synchronized from LeetCode on September 26, 2026.

## Approach & Intuition

> The center of a star appears in every edge, so check whether the first endpoint of the first edge appears in the second edge; if not, the other endpoint is the center.

## Complexity

- **Time Complexity:** `O(1)` — The solution checks membership in an edge containing exactly two vertices, requiring constant time.
- **Space Complexity:** `O(1)` — The solution uses only a constant amount of auxiliary space.
