# Find Center of Star Graph

**Difficulty:** Easy

**Language:** Java

## Problem

https://leetcode.com/problems/find-center-of-star-graph/

## Solution

Automatically synchronized from LeetCode on September 26, 2026.

## Approach & Intuition

> Count the degree of every node by iterating over all edges, then return the unique node whose degree equals n-1, since the center of a star graph is connected to every other node.

## Complexity

- **Time Complexity:** `O(N)` — The algorithm makes one pass over the N-1 edges to build degree counts and one pass over N nodes to find the degree n-1 node, giving linear time.
- **Space Complexity:** `O(N)` — An auxiliary degree array of size N+1 is allocated to store the degree count of each node.
