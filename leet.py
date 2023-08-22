# from typing import List
#
#
# class Solution:
#     """
#     Normal Brut force approach which has time complexity o(n*n) and space complexity O(1)
#     """
#
#     def twoSum_Brutforce(self, nums: List[int], target: int) -> List[int]:
#         for a in range(len(nums)):
#             for b in range(a + 1, len(nums)):
#                 if nums[a] + nums[b] == target:
#                     return [a, b]
#
#     """
#     In this approach used dict to save the data and looked for the variable, which has time complexity o(n*n) and space complexity O(1)
#     """
#
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         processed_number_dict = dict()
#         for a in range(len(nums)):
#             if (target - nums[a]) in processed_number_dict.keys():
#                 return [a, processed_number_dict[target - nums[a]]]
#             else:
#                 processed_number_dict[nums[a]] = a
#
#
# solution = Solution()
#
# nums = [1, 2, 3, 3]
# target = 9
#
# result = solution.twoSum(nums, target);
# print(result)
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x< 0 or (x != 0 and x % 10 == 0):
#             return False
#
#         reversed_num = 0
#         temp = x
#
#         while temp != 0:
#             reversed_num = reversed_num * 10 + temp % 10
#             temp //= 10
#
#         return reversed_num == x
#
#
# solution = Solution()
# x = 121
# result = solution.isPalindrome(x)
#
# print("Result:", result)

class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0

        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i + 1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]

        return ans

solution = Solution()
x = "IV"
result = solution.romanToInt(x)

print("Result:", result)