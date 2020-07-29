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

# class dqNode:
#     def __init__(self, key, val):
#         self.val = val
#         self.key = key
#         self.pre = None
#         self.next = None
 
# class LRUCache:
 
#     # @param capacity, an integer
#     def __init__( self, capacity ):
#         self.capacity = capacity
#         self.curSize = 0    
#         self.keys2valNode = { }   # mapping key to the node that has the value info
#         # dqlist to store <key, value> pairs
#         self.head = dqNode(-1, -1)
#         self.tail = dqNode(-1, -1)
#         self.head.next = self.tail
#         self.tail.pre = self.head
        
#     # util functions    
#     def moveToFirst( self, pnode ):
#         # link pnode.pre and pnode.next
#         if pnode.pre:
#             pnode.pre.next = pnode.next
#         if pnode.next:
#             pnode.next.pre = pnode.pre
#         # move pnode to first
#         pnode.next = self.head.next
#         if self.head.next:
#             self.head.next.pre = pnode
#         self.head.next = pnode
#         pnode.pre = self.head
        
#     def removeLRU( self ):
#         pdel = self.tail.pre
#         pdel.pre.next = self.tail
#         self.tail.pre = pdel.pre
#         del self.keys2valNode[ pdel.key ]
#         del pdel
 
#     def Insert( self, key, value ):
#         newNode = dqNode(key, value)
#         # add to dict
#         self.keys2valNode[ key ] = newNode
#         # insert to first of dqueue
#         self.moveToFirst(newNode)
#     # @return an integer
#     def get(self, key):
#         if key in self.keys2valNode:
#             # get the node that has value info.
#             pvalue = self.keys2valNode[ key ]
#             value =  pvalue.val
#             # change pvalue to be recently visited one
#             self.moveToFirst( pvalue )
#             return value
#         else: 
#             return -1
        
#     # @param key, an integer
#     # @param value, an integer
#     # @return nothing
#     def put( self, key, value ):
#         # if has key, just have to change the value
#         if key in self.keys2valNode:
#             self.keys2valNode[ key ].val = value
#             self.moveToFirst( self.keys2valNode[ key ] )
#         # insert a new key
#         # 1) curSize < capacity, just insert
#         # 2) curSize == capacity, remove LRU and insert
#         else:
#             self.Insert(key, value)
#             if self.curSize < self.capacity:
#                 self.curSize += 1
#             else:
#                 self.removeLRU()
                
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
