1class Solution:
2    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
3        indegree = [0]*numCourses
4        # outdegree = [0]*numCourses
5        adj = [[] for _ in range(numCourses)]
6
7        op=deque()
8        res=[]
9        for i in prerequisites:
10            adj[i[1]].append(i[0])
11            indegree[i[0]]+=1
12            # outdegree[i[1]]+=1
13        for i in range(numCourses):
14            if indegree[i]==0:
15                op.append(i)
16                
17        while (len(op)!=0):
18            done = op.popleft()
19            res.append(done)
20            for neighbour in adj[done]:
21                indegree[neighbour]-=1
22                if indegree[neighbour]==0:
23                    op.append(neighbour)
24        return res