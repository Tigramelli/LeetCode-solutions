class Solution:
    def isPalindrome_str(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]

    def isPalindrome_nostr(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_num = 0
        original_num = x

        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        return original_num == reversed_num
