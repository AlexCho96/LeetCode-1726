from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0

        nums.sort()
        validTuples = 0
        for i in range(len(nums)):
            for j in range(len(nums)-1,i,-1):
                for k in range(i+1,j):
                    for l in range(j-1,k,-1):
                        print(i,j,k,l)
                        if nums[i]*nums[j] == nums[k]*nums[l]:
                            validTuples += 8
                
        return validTuples