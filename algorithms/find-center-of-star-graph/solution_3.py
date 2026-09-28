class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        degree = {}

        for u, v in edges:
            degree[u] = degree.get(u, 0) + 1
            degree[v] = degree.get(v, 0) + 1

        for node in degree:
            if degree[node] == len(edges):
                return node