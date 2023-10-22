# https://www.acmicpc.net/problem/1991
import sys


class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

# 전위
def preorder(target: int):
    if target == -1:
        return

    print(chr(target + ord("A")), end="")
    preorder(nodes[target].left)
    preorder(nodes[target].right)


# 중위
def inorder(target: int):
    if target == -1:
        return

    inorder(nodes[target].left)
    print(chr(target + ord("A")), end="")
    inorder(nodes[target].right)

# 후위
def postorder(target: int):
    if target == -1:
        return

    postorder(nodes[target].left)
    postorder(nodes[target].right)
    print(chr(target + ord("A")), end="")


n = int(input())

# root의 알파벳 아스키코드값을 idx로 쓸거임
# [TODO] 이렇게 안하고 딕셔너리 사용해서 풀어도 될듯!! 그러면 아스키코드값도 안써도 될듯
nodes = [None for _ in range(65)]  

for i in range(n):
    root, left, right = input().rstrip().split()

    root = ord(root) - ord("A")

    if left == ".":
        left = -1
    else:
        left = ord(left) - ord("A")

    if right == ".":
        right = -1
    else:
        right = ord(right) - ord("A")

    node = Node(left, right)
    nodes[root] = node

# A가 항상 루트이므로 0 넣어주면 됨
preorder(0)
print("")

inorder(0)
print("")

postorder(0)
