q= deque()        for i in range(numCourses):            if indegree[i]==0:                q.append(i)        res =[]            node = q.popleft()        while q:            res.append(node)            for neighbour in adj[node]:                if indegree[neighbour]==0:            adj[i[1]].append(i[0])            outdegree[i[1]]+=1            indegree[i[0]]+=1        for i in prerequisites:                    q.append(neighbour)                indegree[neighbour]-=1
        q= deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        res =[]
            node = q.popleft()
        while q:
            res.append(node)
            for neighbour in adj[node]:
                if indegree[neighbour]==0:

            adj[i[1]].append(i[0])
            outdegree[i[1]]+=1
            indegree[i[0]]+=1
        for i in prerequisites:
                    q.append(neighbour)

                indegree[neighbour]-=1