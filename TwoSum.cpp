#include <iostream>
#include <vector>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target);


int main()
{
    vector<int>nums;
    nums.push_back(2);
    nums.push_back(7);
    nums.push_back(11);
    nums.push_back(15);
    int target=9;
    vector<int>obj;
    obj=twoSum(nums, target);
    int i;
    for(i=0;i<obj.size();i++)
    {
        cout<<obj[i]<<" ";
    }

}

vector<int> twoSum(vector<int>& nums, int target)
{
    int i;
    int j;
    vector<int>obj;
    for(i=0;i<nums.size();i++)
    {
        for(j=i+1;j<nums.size();j++)
        {
            if(nums[i]+nums[j]==target)
            {
                obj.push_back(i);
                obj.push_back(j);
                return obj;
            }
        }
    }
    return obj;
}
