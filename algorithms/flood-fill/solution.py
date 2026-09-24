# if (0>i or i>=row and 0>j or>=col): return            col = len(image[0])            if image[i][j] !=clr : return            dfs(image,i+1,j,color)                        image[i][j]=color            if i < 0 or i >= row or j < 0 or j >= col:                return            dfs(image,i-1,j,color)            dfs(image,i,j+1,color)            dfs(image,i,j-1,color)        dfs(image,sr,sc,color)          return image
                # if (0>i or i>=row and 0>j or>=col): return
            col = len(image[0])
            if image[i][j] !=clr : return
            dfs(image,i+1,j,color)
            

            image[i][j]=color
            if i < 0 or i >= row or j < 0 or j >= col:
                return
            dfs(image,i-1,j,color)
            dfs(image,i,j+1,color)
            dfs(image,i,j-1,color)

        dfs(image,sr,sc,color)  

        return image