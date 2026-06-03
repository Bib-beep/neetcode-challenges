from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mostCommon = Counter(nums)
        values = [k[0] for k in mostCommon.most_common(k)]
        return values
