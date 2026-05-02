from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        signature_set = set()
        ret = {}
        for mystr in strs:
            str_sign = tuple(sorted(Counter(mystr).items()))
            if str_sign in ret:
                ret[str_sign].append(mystr)
            else:
                ret[str_sign] = [mystr]
        return list(ret.values())