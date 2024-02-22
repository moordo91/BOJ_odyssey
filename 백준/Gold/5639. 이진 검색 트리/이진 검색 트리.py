import sys
# from collections import deque
# input = sys.stdin.readline
sys.setrecursionlimit(10**5)

preordered_tree = list(map(lambda x: int(x.rstrip()), sys.stdin.readlines()))

def postorder(root_node_idx, left_tree_end_idx):
    global preordered_tree
        
    if root_node_idx > left_tree_end_idx:
        return
    right_tree_start_idx = left_tree_end_idx + 1
    
    for i in range(root_node_idx + 1, left_tree_end_idx + 1):
        if preordered_tree[root_node_idx] < preordered_tree[i]:
            right_tree_start_idx = i
            break
    
    postorder(root_node_idx + 1, right_tree_start_idx - 1)
    postorder(right_tree_start_idx, left_tree_end_idx)
    print(preordered_tree[root_node_idx])
    
postorder(0, len(preordered_tree) - 1)