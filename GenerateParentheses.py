#我原以为是一个全排列，所以写了全排列的代码，但实际上完全忽略了，括号是会重复的，所以并不是全排列
# class Solution:
#     def generateParenthesis(self, n):
#         res=[]
#         if n==0:
#             return res
#         s=[]
#         for i in range(n):
#             s.append('(')
#             s.append(')')
#         stk=[]
#         perm(s,stk,res)
#         # print("0")
#         return res

# def perm(s,stk,res):
#     if not s:
#         res.append(stk)
#     else:
#         for i in range(len(s)):
#             stk.append(s[i])
#             del s[i]
#             perm(s,stk,res)
#             s.insert(i,stk.pop())

#题目里有个要求well-formed parentheses，意思是格式良好的括号，也就是括号是能配对的
#这个条件应该怎么满足，实际上就是l<r就可以，只要每一轮，右括号数量大于左括号，就可以成功配对
class Solution:
    def generateParenthesis(self, n):
        res=[]
        def dfs(s,l,r,res):
            if r<l:
                return
            if l==0 and r==0:
                res.append(s)
                return
            if l>0:
                dfs(s+"(",l-1,r,res)
            if r>0:
                dfs(s+")",l,r-1,res)
        dfs("",n,n,res)
        return res

def main():
    s=Solution
    print(s.generateParenthesis(None,3))

main()

