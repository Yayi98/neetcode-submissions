class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set()
        for elem in nums:
            if elem in myset:
                return True
            myset.add(elem)
        return False