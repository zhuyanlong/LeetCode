class Solution:
    def numIslands(self, grid):
        #保存岛屿数目
        res=0
        if len(grid)==0:
            return res
        visited=[[False for i in range(len(grid[0]))] for j in range(len(grid))]
        lst=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and visited[i][j]==False:
                    lst.append((i,j))
                while lst:
                    dir=[(+1,0),(-1,0),(0,-1),(0,+1)]
                    tmp=lst.pop()
                    visited[tmp[0]][tmp[1]]=True
                    #收集候选解
                    for item in dir:
                        x=item[0]+tmp[0]
                        y=item[1]+tmp[1]
                        if x>=0 and x<len(grid) and y>=0 and y<len(grid[0]):
                            if grid[x][y]=='1' and visited[x][y]==False:
                                lst.append((x,y))
                    if len(lst)==0:
                        res+=1
        return res


def main():
    grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
    s=Solution()
    print(s.numIslands(grid))

main()

# [[True, True, True, True, False], 
# [True, True, False, True, False], 
# [True, True, False, False, False], 
# [False, False, False, False, False]]