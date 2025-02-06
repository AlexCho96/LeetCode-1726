from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0

        product_count = {}
        valid_tuples = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                if product in product_count:
                    valid_tuples += product_count[product]
                    product_count[product] += 1
                else:
                    product_count[product] = 1

        return valid_tuples * 8