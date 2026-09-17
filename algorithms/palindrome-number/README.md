# Palindrome Number

**Difficulty:** Unknown

**Language:** Python3

## Problem

https://leetcode.com/problems/palindrome-number/

## Solution

Automatically synchronized from LeetCode on September 17, 2026.

## Approach & Intuition

> Convert the integer to a string and check whether it is a palindrome by comparing the string directly to its reversed slice.

## Complexity

- **Time Complexity:** `O(log x)` — Converting the integer x to a string and reversing it requires linear time with respect to the number of digits, which is proportional to log10(x).
- **Space Complexity:** `O(log x)` — Creating the string representation and its reversed slice allocates auxiliary memory proportional to the number of digits in x.
