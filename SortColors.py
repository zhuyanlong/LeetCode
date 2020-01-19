#很巧妙的一种算法，应该来说没有普遍性，因为实际上只有三种数，分别是0，1，2，所以我们可以这样去做
#设置前后两个指针，当遇到0的时候，和头指针交换，遇到2，和尾指针交换，遇到1不变，这样子就可以排好序
#或者说这是一种3个数的排序问题
#对于一道算法题，思路要重要得多
#p0和pn之间夹的才是待排序序列
class Solution:
    def sortColors(self, nums):
        if nums == []: 
            return 
        p0 = 0; 
        p2 = len(nums) - 1; 
        i = 0
        while i <=p2:
            if nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i +=1
            else:
                i += 1
        print(nums)

def mnumsin():
    nums=[2,0,2,1,1,0]
    s=Solution
    s.sortColors(None,nums)
mnumsin()

