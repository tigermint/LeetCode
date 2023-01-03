## 풀이 1. 리스트로 변환

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
                
        # 팰린트룸 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True
```
>isalnum() : 영문자, 숫자 여부를 판별하는 함수

>lower() : 소문자로 변환

## 풀이 2. 데크 자료형을 이용한 최적화

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
       # 자료형 데크로 선언
        strs: Deque = collections.deque()
            
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True
```

>Deque: 스택이나 큐처럼 한 방향에서 삽입과 삭제가 일어나는게 아닌 '양방향'에서 삽입과 삭제가 일어나는 자료구조

## 풀이 3. 슬라이싱 사용
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1] # 슬라이싱
```

> 단순히 정규식으로 불필요한 문자를 필터링하고, 문자열을 조작할 수 있는 파이썬의 슬라이싱을 사용했다.  
앞서 isalnum() 으로 모든 문자를 일일이 점검한 코드보다 더 속도를 높일 수 있었다.
