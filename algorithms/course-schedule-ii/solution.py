for i in range(numCourses):            if indegree[i]==0:                q.append(i)        res =[]            node = q.popleft()        while q:        q= deque()            res.append(node)            for neighbour in adj[node]:                indegree[neighbour]-=1                if indegree[neighbour]==0:                    q.append(neighbour)        if len(res)!=numCourses: return []        return res
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        res =[]
            node = q.popleft()
        while q:
        q= deque()
            res.append(node)
            for neighbour in adj[node]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    q.append(neighbour)
        if len(res)!=numCourses: return []
        return res