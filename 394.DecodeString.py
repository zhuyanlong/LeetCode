class Solution:
    def decodeString(self, s):
        if s=='':
            return ''
        stack=[]
        i=0
        while i<len(s):
            tmp=''
            times=''
            if s[i]==']':
                while stack[-1]!='[':
                    tmp=stack.pop()+tmp
                stack.pop()
                while len(stack)>0 and stack[-1]>='0' and stack[-1]<='9':
                    times=stack.pop()+times
                tmp=int(times)*tmp
                for j in range(len(tmp)):
                    stack.append(tmp[j])
            else:
                stack.append(s[i])
            i+=1
        return "".join(stack)


def main():
    s = "3[a2[c]]"
    sol=Solution()
    print(sol.decodeString(s))

main()