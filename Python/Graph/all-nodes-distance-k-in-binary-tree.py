'''
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
dfs를 통해 distance를 구하면 되겠다 라고 생각함
makeGraph를 힌트를 보았다.. 이렇게 하면 되는구나!!
'''

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)   # 바로 연결되어 있는 노드 리스트들 저장해둠

        def makeGraph(node, parent):
            #node, parent 둘다 None이 아닌 경우
            if node and parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            
            # left가 있는 경우
            if node.left:
                makeGraph(node.left, node)
            
            # right가 있는 경우
            if node.right:
                makeGraph(node.right, node)

        makeGraph(root, None)
        

        ans = []
        checked = []

        def dfs(node, dis):
            checked.append(node)

            # 거리가 k면 종료
            if dis == k:
                ans.append(node)
                return
            
            for next_node in graph[node]:
                if next_node not in checked:
                    dfs(next_node, dis +1)

        dfs(target.val, 0)
        return ans
