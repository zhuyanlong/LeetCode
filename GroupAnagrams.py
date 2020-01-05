class Solution:
    def groupAnagrams(self, strs):
        dic={}
        for word in strs:
            sortedword="".join(sorted(word))
            if sortedword in dic:
                dic[sortedword]+=[word]
            else:
                dic[sortedword]=[word]
        res=[]
        for item in dic:
            res.append(dic[item])

        print(res)
        return res

def main():
    strs=["eat", "tea", "tan", "ate", "nat", "bat"]
    s=Solution
    s.groupAnagrams(None,strs)

main()