# Find Center of Star Graph

**Difficulty:** Easy

**Language:** Python3

## Problem

https://leetcode.com/problems/find-center-of-star-graph/

## Solution

Automatically synchronized from LeetCode on September 26, 2026.

## Approach & Intuition

> The center of a star appears in every edge, so check whether the first endpoint of the first edge is in the second edge; if not, return the other endpoint.

## Complexity

- **Time Complexity:** `O(1)` — The algorithm checks membership in a two-element edge and performs a constant number of operations.
- **Space Complexity:** `O(1)` — It uses only a constant amount of auxiliary space.
