#贪心法最经典的实践，如果能够理解，会很快做出来
# class Solution:
#     def canJump(self, nums):
#         step=nums[0]
#         for i in range(1,len(nums)):
#             if step>0:
#                 step-=1
#                 step=max(step,nums[i])
#             else:
#                 return False
#         return True

#第二种方式从后向前遍历，和 从前向后遍历其实没有太大的差别
#每次的检测都是我目前位置上的步数，加上我目前的位置是否大于我目前的位置
#换句话说，我之前的位置能否支持我到当前位置
class Solution:
    def canJump(self, nums):
        current_valid_index = len(nums) - 1
        
        
        for index in range(len(nums) - 1, -1, -1):
            if (nums[index] + index >= current_valid_index):
                if (index == 0):
                    return True
                else:
                    current_valid_index = index
                    
        return False


def main():
    nums=[3,2,1,0,4]
    s=Solution
    print(s.canJump(None,nums))

main()