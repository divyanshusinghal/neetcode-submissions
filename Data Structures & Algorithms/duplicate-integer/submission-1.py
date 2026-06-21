from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums) 
        # data_dict = defaultdict(int)
        # for num in nums:
        #     if data_dict[num] == 0:
        #         data_dict[num]+=1
        #     elif data_dict[num] > 0:
        #         return True
        # return False


        