# Find the Town Judge

**Difficulty:** Easy

**Language:** Python3

## Problem

https://leetcode.com/problems/find-the-town-judge/

## Solution

Automatically synchronized from LeetCode on September 23, 2026.

## Approach & Intuition

> Use degree counting: for each trust pair [a, b], decrement person a's score (they trust someone) and increment person b's score (they are trusted); the town judge is the person whose net score equals n-1, meaning everyone trusts them and they trust no one.

## Complexity

- **Time Complexity:** `O(N + T)` — The algorithm makes a single pass over all T trust relationships to update scores and one pass over N people to find the judge, yielding linear time in people plus trust edges.
- **Space Complexity:** `O(N)` — A single score/count array of size N+1 is allocated to track each person's net trust balance, independent of the number of trust pairs.
