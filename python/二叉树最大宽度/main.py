def widthofBinaryTree(root):
    # 记录节点的深度,值
    quene = [(root, 0, 0)]
    # cur_deepth 当前的深度，left 极左节点的值，target　目标值
    cur_deepth = left = target = 0
    for node, deepth, pos in quene:
        if node:
            quene.append((node.left, deepth+1, 2*pos))
            quene.append((node.right, deepth+1, 2*pos+1))
            # 当深度更改的时候，需要更改当前极左节点的的值
            if cur_deepth != deepth:
                cur_deepth = deepth
                left = pos
            target = max(pos-left+1, target)
    return target
