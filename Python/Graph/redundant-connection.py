'''
크루스칼에서 많이 쓰던 그 부모루트 찾기, 사이클 찾기 활용
edges들 연결하다가 사이클 발생 시 답 출력
'''

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # 부모 루트 찾기
        def find_parent(parent, x):
            if parent[x] != x:
                parent[x] = find_parent(parent, parent[x])
            return parent[x]

        # 연결 -> cycle 체크용
        def union_parent(parent, a, b):
            parent_a = find_parent(parent, a)
            parent_b = find_parent(parent, b)

            if parent_a == parent_b:
                return True

            parent[a] = parent_b
            parent[parent_a] = parent_b
            return False

            # 개선 전
            # if parent_a < parent_b:
            #     parent[b] = parent_a
            #     parent[parent_b] = parent_a
            # else:
            #     parent[a] = parent_b
            #     parent[parent_a] = parent_b

        parent = [i for i in range(len(edges) + 1)] # 가장 처음 parent는 자기자신
        
        for edge in edges:
            n1 = edge[0]
            n2 = edge[1]

            n1_parent = find_parent(parent, n1)
            n2_parent = find_parent(parent, n2)

            # cycle 발생
            if union_parent(parent, n1, n2):
                return edge
