## 풀이1. 람다와 + 연산자를 이용
```python
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 문자와 숫자 로그 구분
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                
        # 2개의 키를 람다 표현식으로 정렬
        # x를 자른 식별자 제외한 것들로 정렬 -> 같을 경우 식별자로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
```

> 문자로 구성된 로그가 숫자 로그보다 이전, 숫자 로그는 입력 순서대로 둔다.  
따라서, 문자와 숫자를 구분하고, 숫자는 나중에 이어붙인다.

