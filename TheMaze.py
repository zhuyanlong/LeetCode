#BFS 使用队列
#DFS 使用栈
class Solution:
    def hasPath(self, maze, start, destination):
        queue=[]
        visited={}
        visited[(start[0],start[1])]=True
        queue.append(start)
        while(len(queue)!=0):
            s=queue[0]
            queue.pop(0)
            dirs=[[0,-1],[0,1],[-1,0],[1,0]]
            for d in dirs:
                x=d[0]+s[0]
                y=d[1]+s[1]
                if x==destination[0] and y==destination[1]:
                    return True
                if x>=0 and y>=0 and x<len(maze) and y<len(maze[0]) and maze[x][y]!=1 and not ((x,y) in visited.keys()):
                    queue.append([x,y])
                    visited[(x,y)]=True
        return False

def main():
    maze=[[0,0,1,0,0],
          [0,0,1,0,0],
          [0,0,0,1,0],
          [1,1,0,1,1],
          [0,0,0,0,0]
          ]
    start=[2,1]
    destination=[4,4]
    s=Solution()
    print(s.hasPath(maze,start,destination))

main()