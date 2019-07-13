dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

class Solution:
    def romanToInt(self, s: str) -> int:
       sum=0
       i=0

       #在python的for循环里，下标的变化，是不太明确的
       while i!=len(s):
          if i+1<len(s):
             if s[i:i+2] in dic:
                 sum+=dic[s[i:i+2]]
                 i+=1
             else:
                 sum+=dic[s[i]]
          else:
             sum+=dic[s[i]]
          i+=1
          print(i,sum)
       return sum

def main():
    s="LVIII"
    print(Solution.romanToInt(s,s))

main()
