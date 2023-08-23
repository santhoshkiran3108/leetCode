class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x< 0 or (x != 0 and x % 10 == 0):
            return False

        reversed_num = 0
        temp = x

        while temp != 0:
            reversed_num = reversed_num * 10 + temp % 10
            temp //= 10

        return reversed_num == x


solution = Solution()
x = 121
result = solution.isPalindrome(x)

print("Result:", result)

