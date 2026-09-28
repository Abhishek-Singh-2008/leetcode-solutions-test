class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        common = set(edges[0]) & set(edges[1])
        return common.pop()