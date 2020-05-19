class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack=[]
        maxlen=0
        last=-1
        for i in range(len(s)):
            # print(stack)
            if s[i]=="(":
                stack.append(i)
            else:
                if len(stack)==0:
                    last=i
                else:
                    stack.pop()
                    if len(stack)==0:
                        maxlen=max(maxlen,i-last)
                        # print(i)
                    else:
                        maxlen=max(maxlen,i-stack[len(stack)-1])
        return maxlen

t="()((()))"
s=Solution
print(s.longestValidParentheses(s,t))