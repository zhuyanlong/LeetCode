class LRUCache:
    def __init__(self, capacity):
        self.capacity=capacity
        self.lst=[]
        self.dict={}
        self.lenght=0

    def get(self, key):
        if key not in self.dict:
            return -1
        else:
            self.lst.remove(key)
            self.lst.append(key)
            return self.dict[key]

    def put(self, key: int, value: int) -> None:
        #如果使用缓存中的数据
        if key in self.lst:
            self.lst.remove(key)
            self.lst.append(key)
            self.dict[key]=value
        else:
            #如果list已满，则需要抛弃元素
            if len(self.lst)==self.capacity:
                tmp=self.lst.pop(0)
                del self.dict[tmp]
                self.lst.append(key)
                self.dict[key]=value
            else:
                self.lst.append(key)
                self.dict[key]=value

def main():
    cache=LRUCache(2)
    cache.put(1,1)
    cache.put(2,2)
    print(cache.get(1))
    cache.put(3,3)
    print(cache.get(2))
    cache.put(4,4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))

main()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)