class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inverted_list = [target - i for i in nums]
        for i, num in enumerate(nums):
            for j, inv in enumerate(inverted_list):
                if num == inv:
                    if i != j:
                        return [i, j]
