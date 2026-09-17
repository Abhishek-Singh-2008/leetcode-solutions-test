# Two Sum

**Difficulty:** Unknown

**Language:** Python3

## Problem

https://leetcode.com/problems/two-sum/

## Solution

Automatically synchronized from LeetCode on September 17, 2026.

## Approach & Intuition

> Uses a one-pass hash map to store previously seen numbers and their indices, checking at each step if the complement (target - num) has already been encountered.

## Complexity

- **Time Complexity:** `O(N)` — We iterate through the array of N elements once, performing O(1) average-time dictionary lookups and insertions for each element.
- **Space Complexity:** `O(N)` — In the worst case, the hash map stores up to N elements if the matching pair is found at the very end.
