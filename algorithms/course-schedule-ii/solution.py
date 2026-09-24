q= deque()        for i in range(numCourses):            if indegree[i]==0:                q.append(i)        res =[]            node = q.popleft()        while q:            adj[i[1]].append(i[0])            outdegree[i[1]]+=1            indegree[i[0]]+=1        for i in prerequisites:        adj = [[] for _ in range(numCourses)]        if len(adj)<numCourses: return []        outdegree = [0]*numCourses        indegree = [0]*numCourses    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:class Solution:
        q= deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        res =[]
            node = q.popleft()
        while q:

            adj[i[1]].append(i[0])
            outdegree[i[1]]+=1
            indegree[i[0]]+=1
        for i in prerequisites:
        adj = [[] for _ in range(numCourses)]
        if len(adj)<numCourses: return []
        outdegree = [0]*numCourses
        indegree = [0]*numCourses
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
class Solution: