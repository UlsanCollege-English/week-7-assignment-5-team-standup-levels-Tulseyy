from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    # TODO: return list of lists
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res

def zigzag_level_order(root):
    # TODO
    if not root:
        return []
    res = []
    q = deque([root])
    left_to_right = True
    while q:
        level = deque()
        for _ in range(len(q)):
            node = q.popleft()
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(list(level))
        left_to_right = not left_to_right
    return res

def right_side_view(root):
    # TODO
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        last = None
        for _ in range(len(q)):
            node = q.popleft()
            last = node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(last)
    return res
