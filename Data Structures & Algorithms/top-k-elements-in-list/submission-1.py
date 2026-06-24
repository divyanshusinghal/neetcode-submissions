import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results_dict = {}
        for num in nums:
            if num in results_dict:
                results_dict[num] = results_dict.get(num, 0) + 1 
            else:
                results_dict[num] = 1
        print(results_dict)

        results_tuple = []
        for num, count in results_dict.items():
            results_tuple.append((count, num))

        output = heapq.nlargest(k, results_tuple)
        print(output)
        # c = Counter(nums)
        # output = c.most_common(k)
        return [elem[1] for elem in output]