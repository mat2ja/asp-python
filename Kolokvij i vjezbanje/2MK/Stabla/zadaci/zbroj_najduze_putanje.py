from binarytree import Node

import math


def SumOfLongRootToLeafPath_util(root, Sum, Len, maxLen, maxSum):
    if not root:
        if maxLen[0] < Len:
            maxLen[0] = Len
            maxSum[0] = Sum
        elif maxLen[0] == Len and maxSum[0] < Sum:
            maxSum[0] = Sum
        return

    Sum += root.value
    Len += 1

    SumOfLongRootToLeafPath_util(root.left, Sum, Len, maxLen, maxSum)

    SumOfLongRootToLeafPath_util(root.right, Sum, Len, maxLen, maxSum)


def SumOfLongRootToLeafPath(root):
    if not root:
        return 0

    maxSum = [-math.inf]
    maxLen = [0]

    SumOfLongRootToLeafPath_util(root, 0, 0, maxLen, maxSum)

    return maxSum[0]


root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(7)
root.left.right = Node(1)
root.right.left = Node(2)
root.right.right = Node(3)
root.left.right.left = Node(6)

print(root)

print(SumOfLongRootToLeafPath(root))
