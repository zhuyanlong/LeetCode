#这种方法很蠢，但是时间复杂度极低
dic={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}

class Solution:
    def intToRoman(self, num: int) -> str:
        re=''
        while num!=0:
         if num>=1000:
            num-=1000
            re+=dic[1000]
         elif num>=900:
            num-=900
            re+=dic[900]
         elif num>=500:
            num-=500
            re+=dic[500]
         elif num>=400:
            num-=400
            re+=dic[400]
         elif num>=100:
            num-=100
            re+=dic[100]
         elif num>=90:
            num-=90
            re+=dic[90]
         elif num>=50:
            num-=50
            re+=dic[50]
         elif num>=40:
            num-=40
            re+=dic[40]
         elif num>=10:
            num-=10
            re+=dic[10]
         elif num>=9:
            num-=9
            re+=dic[9]
         elif num>=5:
            num-=5
            re+=dic[5]
         elif num>=4:
            num-=4
            re+=dic[4]
         else:
            num-=1
            re+=dic[1]
        return re

def main():
    s=58
    print(Solution.intToRoman(s,s))

main()


