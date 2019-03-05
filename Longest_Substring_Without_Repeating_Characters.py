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

def main():
	s=Solution()
	s.lengthOfLongestSubstring("pwwkew")

main()