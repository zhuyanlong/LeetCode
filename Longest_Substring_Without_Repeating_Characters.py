class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		result=0
		for i in range(len(s)):
			tmp=""+s[i]
			for j in range(i+1,len(s)):
				if s[j] in tmp:
					break
				else:
					tmp+=s[j]
			num=len(tmp)
			if num>result:
				result=num
		return result

#寻找最长不重复字符串，采用滑动区间复杂度较高
class Solution:
    def lengthOfLongestSubstring(self, s):
        mac=0
        i=0
        tmp=[]
        while i!=len(s):
            if s[i] in tmp:
                tmp=tmp[tmp.index(s[i])+1:]
            tmp.append(s[i])
            if len(tmp)>mac:
                mac=len(tmp)
            i+=1
        return mac

def main():
	s=Solution()
	s.lengthOfLongestSubstring("pwwkew")

main()
