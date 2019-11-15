from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            print (i)
            if target-nums[i] in dict:
                print(dict)
                return [dict[target-nums[i]], i]
            else:
                dict[nums[i]] = i
l1=[2,7,9,11,15]
t1=17
a=Solution()
print(a.twoSum(l1,t1))