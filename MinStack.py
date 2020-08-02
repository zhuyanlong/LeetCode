#高空间复杂度，低时间复杂度
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.val=[]
        self.minval=[float('inf')]

    def push(self, x: int) -> None:
        self.val.append(x)
        if x<=self.minval[-1]:
            self.minval.append(x)

    def pop(self) -> None:
        tmp=self.val[-1]
        del self.val[-1]
        if tmp==self.minval[-1]:
            del self.minval[-1]

    def top(self) -> int:
        return self.val[-1]

    def getMin(self) -> int:
        return self.minval[-1]

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.val=[]

    def push(self, x: int) -> None:
        self.val.append(x)


    def pop(self) -> None:
        del self.val[-1]

    def top(self) -> int:
        return self.val[-1]

    def getMin(self) -> int:
        return min(self.val)

def main():
    ms=MinStack()
    ms.push(0)
    ms.push(1)
    ms.push(0)
    print(ms.getMin())
    ms.pop()
    print(ms.top())
    print(ms.getMin())
main()


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()