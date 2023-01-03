class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for item in s:
            if item.isalnum():
                strs.append(item.lower())
        
        index = 0
        while index < len(strs) / 2:
            if strs[index] != strs[len(strs) - index - 1]:
                return False
            index += 1
        return True