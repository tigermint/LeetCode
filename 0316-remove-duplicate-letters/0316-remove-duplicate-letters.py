class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 집합으로 정렬
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            # 전체 집합과 접미사 집합 일치시 분리 진행
            if set(suffix) == set(s): # 해당 char 이후 존재하는게 없다?
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''
