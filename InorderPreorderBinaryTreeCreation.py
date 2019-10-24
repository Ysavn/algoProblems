#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

# O(n) solution using map
# Problem link in codesignal - https://app.codesignal.com/interview-practice/task/AaWaYxi8gjtbqgp2M
pre_idx = [0]
mp = {}
def restoreBinaryTreeHelper(inorder, preorder, s, e):
    if s > e:
        return None
    t = Tree(preorder[pre_idx[0]])
    m = mp[preorder[pre_idx[0]]]
    pre_idx[0] += 1
    t.left = restoreBinaryTreeHelper(inorder, preorder, s, m-1)
    t.right = restoreBinaryTreeHelper(inorder, preorder, m+1, e)
    return t

def restoreBinaryTree(inorder, preorder):
    n = len(inorder)
    for i, inval in enumerate(inorder):
        mp[inval] = i
    return restoreBinaryTreeHelper(inorder, preorder, 0, n-1)

