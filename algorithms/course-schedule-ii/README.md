# Course Schedule II

**Difficulty:** Medium

**Language:** Python3

## Problem

https://leetcode.com/problems/course-schedule-ii/

## Solution

Automatically synchronized from LeetCode on September 23, 2026.

## Approach & Intuition

> Use Kahn's topological sort: build an adjacency list and indegree counts, enqueue all courses with indegree 0, then repeatedly pop a course, append it to the order, and decrement neighbors' indegrees, enqueuing any that become 0.

## Complexity

- **Time Complexity:** `O(V + E)` — Each vertex is enqueued and dequeued once, and each prerequisite edge is processed once, where V = numCourses and E = len(prerequisites).
- **Space Complexity:** `O(V + E)` — The adjacency list stores O(V + E) edges/vertices, while the indegree array and queue use O(V) auxiliary space, excluding the returned order.
