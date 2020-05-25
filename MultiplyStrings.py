#python has built-in big integer module, it can compute directly
# class Solution:
#     def multiply(self, num1, num2):
#         return str(int(num1)*int(num2))


class Solution:
    def multiply(self, num1, num2):
        num1=num1[::-1]
        num2=num2[::-1]
        num1=list(num1)
        num2=list(num2)
        res=[0 for i in range(len(num1)+len(num2))]
        #multiply
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i+j]+=int(num1[i])*int(num2[j])
        #carry

        for i in range(len(res)-1):
            res[i+1]+=res[i]//10
            res[i]=res[i]%10
            # print("i",res[i])
            # print("i+1",res[i+1])
        k=len(res)-1
        while res[k]==0 and k!=0:
            res.pop()
            k-=1
        a=''
        for i in range(len(res)):
            a+=str(res[i])
        a=a[::-1]
        return a

def main():
    str1="000"
    str2="00"
    s=Solution
    print(s.multiply(s,str1,str2))

main()