from collections import deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inOrderTraversal(root):
    if root is None:
        return

    inOrderTraversal(root.left)
    print(root.data)
    inOrderTraversal(root.right)


def preOrderTraversal(root):
    if root is None:
        return

    print(root.data)
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)


def postOrderTraversal(root):
    if root is None:
        return

    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.data)


# Leetcode - Problem: 

def maxDepthOfTree(root):
    if root is None:
        return 0

    left = maxDepthOfTree(root.left)
    right = maxDepthOfTree(root.right)

    return max(left, right) + 1


# Leetcode - Problem: 110

def isTreeBalanaced(root):
    def checkBalance(root):
        if root is None:
            return 0

        left = checkBalance(root.left)
        right = checkBalance(root.right)

        if left == -1 or right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return max(left, right) + 1

    res = checkBalance(root)
    return False if res == -1 else True


# Leetcode - Problem: 236

def lowestCommonAncestor(root, k, v):
    if root is None or root == k or root == v:
        return root

    left = lowestCommonAncestor(root.left, k, v)
    right = lowestCommonAncestor(root.right, k, v)

    if not left:
        return right
    elif not right:
        return left
    else:
        return root


# Leetcode - Problem: 543

def diameterOfATree(root):
    diameter = [float("-inf")]
    def calculateDiameter(root):
        if root is None:
            return 0

        left = calculateDiameter(root.left)
        right = calculateDiameter(root.right)

        diameter[0] = max(diameter[0], left+right)

        return max(left, right) + 1

    calculateDiameter(root)
    return diameter[0]


# Leetcode - Problem: 102

def levelOrderTraversal(root):
    if root is None:
        return

    res = []
    queue = deque()

    queue.append(root)
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            level.append(node.data)
        res.append(level)
    return res


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(7)
# root.right.right = TreeNode(8)
# root.right.right.right = TreeNode(11)
# root.right.right.right.right = TreeNode(15)


# BST

# Leetcode - Problem: 230

def topKSmallestNode(root, k):
    res = []
    def traverseTree(root):
        if root is None:
            return

        traverseTree(root.left)
        res.append(root.data)
        traverseTree(root.right)

    traverseTree(root)
    return res[k-1]


def topKLargestNode(root, k):
    res = []
    def traverseTree(root):
        if root is None:
            return

        traverseTree(root.left)
        res.append(root.data)
        traverseTree(root.right)

    traverseTree(root)
    return res[len(res) - res[k-1]]


# bst_root = TreeNode(5)
# bst_root.left = TreeNode(3)
# bst_root.right = TreeNode(7)
# bst_root.left.left = TreeNode(1)
# bst_root.left.right = TreeNode(4)
# bst_root.right.left = TreeNode(6)
# bst_root.right.right = TreeNode(8)
# bst_root.left.left.right = TreeNode(2)
