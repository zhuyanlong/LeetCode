class Solution:
    def trap(self, height):
        leftmosthigh=[0 for i in range(len(height))]
        rightmosthigh=[0 for i in range(len(height))]
        leftmax=0
        rightmax=0
        for i in range(len(height)):
            if height[i]>leftmax:
                leftmax=height[i]
            leftmosthigh[i]=leftmax
        for i in reversed(range(len(height))):
            if height[i]>rightmax:
                rightmax=height[i]
            rightmosthigh[i]=rightmax
        result=0
        for i in range(len(height)):
            volume=min(leftmosthigh[i],rightmosthigh[i])
            if volume>height[i]:
                result+=volume-height[i]
        return result

def main():
    s=Solution
    height=[0,1,0,2,1,0,1,3,2,1,2,1]
    print(s.trap(s,height))

main()