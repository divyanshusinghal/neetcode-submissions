class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_vals_index= {}
        for index_i, i in enumerate(nums):
            dict_vals_index[i] = index_i

        for index_i, i in enumerate(nums):
            j = target - i
            if j in dict_vals_index and dict_vals_index[j] != index_i:
                return [index_i, dict_vals_index[j]]
            
        return []
