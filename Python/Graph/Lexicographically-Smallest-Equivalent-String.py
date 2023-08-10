'''
문제 이해가 어마어마하게 오래걸린 문제...
개인적으로 이런 그래프문제에 dict보단 배열쓰는게 좋아서
아스키코드값을 idx로 사용해서 풀었는데, ord('a')가 계속 반복되는게 안좋아보임...
'''

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find_parent(x):
            if parent[x] != x:
                parent[x] = find_parent(parent[x])
            
            return parent[x]

        def union(a, b):
            parent_a = find_parent(a)
            parent_b = find_parent(b)

            if parent_a > parent_b:
                parent[parent_a] = parent_b
            
            else:
                parent[parent_b] = parent_a

        parent = [i for i in range(26)]
        
        for i in range(0, len(s1)):
            a = ord(s1[i]) - ord('a')
            b = ord(s2[i]) - ord('a')
            union(a, b)
        
        ans = []
        for base in baseStr:
            base = ord(base) - ord('a')
            base = find_parent(base) + ord('a')
            ans.append(chr(base))

        return "".join(ans)
    
