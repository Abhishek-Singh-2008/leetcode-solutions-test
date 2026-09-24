# Course Schedule II

**Difficulty:** Medium

**Language:** Python3

## Problem

https://leetcode.com/problems/course-schedule-ii/

## Solution

Automatically synchronized from LeetCode on September 24, 2026.

## Approach & Intuition

> Build an adjacency list and indegree counts, then apply Kahn's algorithm (BFS topological sort) by repeatedly enqueuing courses with indegree 0 and appending them to the result.

## Complexity

- **Time Complexity:** `O(V + E)` — Each course is enqueued and dequeued once, and each prerequisite edge is processed once.
- **Space Complexity:** `O(V + E)` — The adjacency list uses O(V + E) space, while indegree/outdegree arrays and the queue use O(V) auxiliary space.
