# Container With Most Water

**Difficulty:** Medium

**Language:** Python3

## Problem

https://leetcode.com/problems/container-with-most-water/

## Solution

Automatically synchronized from LeetCode on September 20, 2026.

## Approach & Intuition

> Uses a two-pointer technique starting from both ends of the array, computing the container area at each step and greedily moving the pointer at the shorter line inward, since the area is bounded by the shorter height and only moving it could possibly yield a larger area.

## Complexity

- **Time Complexity:** `O(N)` — Each iteration of the while loop moves one pointer inward by one position, so the loop runs at most N-1 times with O(1) work per iteration.
- **Space Complexity:** `O(1)` — Only a fixed number of scalar variables (left, right, ans, width, h, area) are used regardless of input size, with no auxiliary data structures or recursion.
