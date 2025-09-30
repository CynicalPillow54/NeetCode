#Valid Anagram
#Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for char in range(len(s)):
            count[ord(s[char]) - ord('a')] += 1
            count[ord(t[char]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True


if __name__ == '__main__':
    s = "fe"
    t = "ja"
    result = Solution().isAnagram(s, t)
    print(result)


