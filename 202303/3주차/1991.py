# 트리 순회
from sys import stdin


def preorder(root):    # 전위 순회: root -> left -> right
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])


def inorder(root):  # 중위 순회: left -> root -> right
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])


def postorder(root):    # 후위 순회: left -> right -> root
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')


n = int(stdin.readline())
tree = {}

for _ in range(n):
    root, left, right = stdin.readline().split()
    tree[root] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')
