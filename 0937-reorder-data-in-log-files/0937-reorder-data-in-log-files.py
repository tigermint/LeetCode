class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 문자와 숫자 로그 구분
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                
        # 2개의 키를 람다표현식으로 정렬
        # x를 자른 식별자 제외한 것들로 정렬 -> 같을 경우 식별자로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits