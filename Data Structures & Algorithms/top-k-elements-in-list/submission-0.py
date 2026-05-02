from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = Counter(nums)
        xx=tuple(sorted((freqmap[key],key) for key in freqmap)[::-1])
        print(xx)
        return [xx[i][1] for i in range(k)]