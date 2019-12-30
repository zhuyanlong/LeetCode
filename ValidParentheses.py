class Solution:
    def isValid(self, s):
        lst1=[]
        lst2=[]
        if len(s)==0:
            return True
        for i in range(len(s)):
            lst1.append(s[i])
        while len(lst1)!=0:
            tmp=lst1.pop()
            print("lst1",tmp)
            if tmp==')' or tmp==']' or tmp=='}':
                lst2.append(tmp)
            else:
                if len(lst2)==0:
                    return False
                tmp2=lst2.pop()
                print("lst2",tmp2)
                if tmp=='(':
                    if tmp2!=')':
                        return False
                elif tmp=='[':
                    if tmp2!=']':
                        return False
                elif tmp=='{':
                    if tmp2!='}':
                        return False
        if len(lst2)!=0:
            return False
        return True


def main():
    s=Solution
    print(s.isValid(None,"{{)}"))
main()