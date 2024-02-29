from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            ana[key].append(s)

        return list(ana.values())
