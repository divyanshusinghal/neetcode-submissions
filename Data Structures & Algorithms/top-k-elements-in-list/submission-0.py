from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        output = c.most_common(k)
        return [elem[0] for elem in output]