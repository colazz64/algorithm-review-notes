class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = {}

        for ch in s:
            counter[ch] = counter.get(ch, 0) + 1

        for ch in t:
            if ch not in counter:
                return False

            if counter[ch] == 1:
                counter.pop(ch)
            else:
                counter[ch] -= 1

        return len(counter) == 0
