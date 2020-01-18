#这道题的想法很简单，类似于之前做的进位题，因为是加法，所以很容易，只用从最后一位开始就行
class Solution:
    def addBinary(self, a, b):
        num1=len(a)-1
        num2=len(b)-1
        carry=0
        res=""
        while num1!=-1 and num2!=-1:
            tmp=(int(a[num1])-int('0'))+(int(b[num2])-int('0'))
            if tmp==2:
                if tmp+carry==2:
                    res="0"+res
                else:
                    res="1"+res
                carry=1
            else:
                if tmp+carry==2:
                    res="0"+res
                    carry=1
                elif tmp+carry==1:
                    res="1"+res
                    carry=0
                else:
                    res="0"+res
                    carry=0
            num1-=1
            num2-=1
        # print(res)
        while num1!=-1:
            tmp=int(a[num1])
            if tmp+carry==2:
                res="0"+res
                carry=1
            elif tmp+carry==1:
                res="1"+res
                carry=0
            else:
                res="0"+res
                carry=0
            num1-=1
        while num2!=-1:
            tmp=int(b[num2])
            if tmp+carry==2:
                res="0"+res
                carry=1
            elif tmp+carry==1:
                res="1"+res
                carry=0
            else:
                res="0"+res
                carry=0
            num2-=1
        if carry==1:
            res="1"+res
        return res

def main():
    s=Solution
    a="1"
    b="111"
    print(s.addBinary(None,a,b))

main()



