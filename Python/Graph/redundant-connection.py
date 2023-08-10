'''
https://leetcode.com/problems/redundant-connection/
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

            # 개선완료
            # 8/10 -> parent[a] = parent_b 이런 코드는 불필요함. 의미없음!! 오히려 의도에 맞지않는 코드임. 왜 이렇게 했을까..?
            # 맨 처음 하고싶었던 의도대로, 작은 노드를 기준으로 부모 정하도록 해줌
            if parent_a > parent_b:
                parent[parent_a] = parent_b
            else:
                parent[parent_b] = parent_a
            return False

            # 개선 전2
            # parent[a] = parent_b
            # parent[parent_a] = parent_b

            # 개선 전1
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
