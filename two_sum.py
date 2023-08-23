from typing import List
class Solution:
    """
    Normal Brut force approach which has time complexity o(n*n) and space complexity O(1)
    """

    def twoSum_Brutforce(self, nums: List[int], target: int) -> List[int]:
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                if nums[a] + nums[b] == target:
                    return [a, b]

    """
    In this approach used dict to save the data and looked for the variable, which has time complexity o(n*n) and space complexity O(1)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        processed_number_dict = dict()
        for a in range(len(nums)):
            if (target - nums[a]) in processed_number_dict.keys():
                return [a, processed_number_dict[target - nums[a]]]
            else:
                processed_number_dict[nums[a]] = a


solution = Solution()

nums = [1, 2, 3, 3]
target = 9

result = solution.twoSum(nums, target);
print(result)