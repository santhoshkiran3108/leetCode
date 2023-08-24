from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        for i in range(len(strs[0])):
            sym = strs[0][i]

            for s in strs:
                try:
                    print(s[i])
                    print(sym)
                    if s[i] != sym:
                        print("here")
                        return strs[0][:i]
                except IndexError:
                    return strs[0][:i]
        return strs[0]


solution = Solution()
x = ["flower", "flow", "flight"]
result = solution.longestCommonPrefix(x)

print("Result:", result)
