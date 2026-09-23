# Course Schedule II

**Difficulty:** Medium

**Language:** Python3

## Problem

https://leetcode.com/problems/course-schedule-ii/

## Solution

Automatically synchronized from LeetCode on September 23, 2026.

## Approach & Intuition

> Kahn's algorithm for topological sorting: build an adjacency list and indegree array, enqueue all courses with indegree 0, then repeatedly dequeue a course, append it to the order, and decrement the indegree of its neighbors.

## Complexity

- **Time Complexity:** `O(V + E)` — Each course vertex is enqueued and dequeued at most once, and each prerequisite edge is processed exactly once.
- **Space Complexity:** `O(V + E)` — The adjacency list stores all E edges plus V lists, while the indegree array and queue store up to V courses each.
