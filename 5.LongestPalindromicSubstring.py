def longestPalindrome( s: str) -> str:
	start=0
	end=0
	for i in range(len(s)):
		len1=expandAroundCenter(s,i,i)
		len2=expandAroundCenter(s,i,i+1)
		lens=max(len1,len2)
		if (end-start+1) <lens:
			start=int(i-(lens/2)+1)
			end=int(i+lens/2)

	return s[start:end+1]


def expandAroundCenter(s, left, right):
	while left>=0 and right <len(s) and s[left]==s[right]:
		left-=1
		right+=1
	left+=1
	right-=1
	return right-left+1

def main():
	s="babad"
	print(longestPalindrome(s))

main()
