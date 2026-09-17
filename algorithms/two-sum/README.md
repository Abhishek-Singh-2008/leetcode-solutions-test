# Two Sum

**Difficulty:** Easy

**Language:** Python3

## Problem

https://leetcode.com/problems/two-sum/

## Solution

Automatically synchronized from LeetCode on September 17, 2026.

## Approach & Intuition

> Uses a one-pass hash map to store each number's index, checking at each step whether the current value's complement (target - num) has already been seen.

## Complexity

- **Time Complexity:** `O(N)` — Iterating through the array of N elements takes linear time, with each hash table lookup and insertion taking O(1) on average.
- **Space Complexity:** `O(N)` — The hash table stores up to N key-value pairs in the worst case where no pair is found until the end of the array.
