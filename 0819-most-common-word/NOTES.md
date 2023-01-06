## 풀이1. 리스트 컴프리헨션, Counter 객체 사용
```python
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                 .lower().split()
                    if word not in banned]
        
        counts = collections.Counter(words)
        #가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]        
```

1. 입력값에는 대소문자가 섞여 있으며 쉼표 및 구두점이 존재한다.  
따라서, 먼저 정규표현식을 이용해서 `단어문자`가 아닌 모든 문자를 공백으로 치환한다.  

2. 아울러 리스트 컴프리헨션의 조건절에는 banned에 포함되지 않는 단어만을 대상으로 한다.  

3. words에는 소문자, 구두점을 제외하고 banned를 제외한 단어 목록이 저장된다. 

이후 개수를 비교하여 가장 흔한 단어를 추출한다.

방법 1.
```python
counts = collections.defaultdict(int)
for word in words:
       counts[word] += 1 # defaultdict 를 사용해 int 기본 값이 자동으로 부여되게 하고 빈도를 확인한다.
return max(counts, key = counts.get) # counts 값이 가장 큰 키를 가져온다
```
방법 2.
```python
counts = collections.Counter(words) # Counter 모듈을 사용하면 좀 더 깔끔하게 처리할 수 있다.
  return counts.most_common(1)[0][0]
```
