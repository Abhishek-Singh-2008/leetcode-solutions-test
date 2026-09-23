for i in range(numCourses):            if indegree[i]==0:                op.append(i)                        while (len(op)!=0):            done = op.popleft()            res.append(done)            for neighbour in adj[done]:                indegree[neighbour]-=1                if indegree[neighbour]==0:                    op.append(neighbour)        return res
        for i in range(numCourses):
            if indegree[i]==0:
                op.append(i)
                
        while (len(op)!=0):
            done = op.popleft()
            res.append(done)
            for neighbour in adj[done]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    op.append(neighbour)
        return res