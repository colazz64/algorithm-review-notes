class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        ans = 0

        for i in range(len(s)):
            if s[i] in vowels:
                count += 1

            if i < k - 1:
                continue

            ans = max(ans, count)

            if s[i - k + 1] in vowels:
                count -= 1

        return ans
