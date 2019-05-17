#!/usr/bin/python
# coding:utf-8
'''  RBTree '''
class RBNode:
    def __init__(self,val,color='R'):
        self.value=value
        self.color=color
        self.left=None
        self.right=None
        self.parent=None
    def is_black_node(self):
        return self.color=='B'
    def set_black_node(self):
        self.color = 'B'
    def set_red_node(self):
        self.color = 'R'
    def print(self):
        if self.left:
            self.left.print()
        print(self.val)
        if self.right:
            self.right.print()

class RBTree:
    '''
    红黑树性质：
    1.根节点是黑色
    2.叶节点是黑色
    3.节点可以上黑色或红色
    4.每个红色的节点的两个子节点是黑色
    5.从任一节点到每个叶节点的所有路径包含相同的黑色节点
    ***从根到叶子的最长路径不多于最短路径的两倍长
    '''
    def __init__(self):
        self.root = None
    def left_rotate(self,node):
        '''
        *左旋示意图
        *    parent                        parent
        *    /                               /
        *  node                           right
        *  /  \                           /   \
        * ln  right       》》》         node   ry
        *     /  \                      /  \
        *    ly  ry                    ln  ly
        *node为要左旋的节点
        *
        '''
        parent = node.parent
        right = node.right

        node.right=right.left     #ly
        if node.right:
            node.right.parent=None
        right.left=node
        node.parent=right

        right.parent = parent
        if not parent:
            self.root = right
        else:
            if parent.left == node:
                parent.left=right
            else:
                parent.right = right
        pass

    def right_rotate(self,node):
        '''
        *右旋示意图
        * right rotate
        *       parent                    parent
        *       /                          /
        *     node                      left
        *     /   \                     /   \
        *   left  ry    >>>>>>>>       ln   node
        *   /   \                           /  \
        *  ln   rn                         rn  ry
        *
        '''
        parent = node.parent
        left = node.left

        node.left = left.right
        if node.left:
            node.left.parent = node

        left.parent=parent
        if not parent:
            self.root = left
        else:
            if parent.left == node:
                parent.left = left
            else:
                parent.right = left
        pass
    def insert_node(self,node):
        '''
        *在树中增加一个红色节点，因为增加黑色节点会使路径上多一个额外的黑色节点，调整更困难
        '''
        if not self.root:
            self.root = node
            return
        cur = self.node
        while cur:
            if cur.val < node.val:
                if not cur.right:
                    node.parent = cur
                    cur.right = node
                    break
                cur = cur.right
                continue
            else:
                if not cur.left:
                    node.parent = cur
                    cur.left = node
                    break
                cur = cur.left
        self.insert_fixup(node)
    def insert_fixup(self,node):
        '''
        *根据性质，整理树形结构
        '''
        if self.root == node or self.root == node.parent   #如果是父节点，设置成黑色节点
            self.root.set_black_node()
            print("set black", node.value)
            return
        if node.parent.is_black_node():     #如果父节点是黑色，直接退出
            return
        grand = node.parent.parent           #如果父节点的兄弟节点也是红色节点
        if not grand:
            self.insert_fixup(node.parent)
            return
        if grand.left and grand.left.is_red_node() and grand.right and grand.right.is_red_node():
            grand.left.set_black_node()
            grand.right.set_black_node()
            grand.set_red_node()
            self.insert_fixup(grand)
            return
        #如果父节点的兄弟节点也是黑色节点
        parent = node.parent                    # node, node.parent, node.parent.parent不同边
        if parent.left == node and grand.right == node.parent:
            self.right_rotate(node.parent)
            self.insert_fixup(parent)
            return
        if parent.right == node and grand.left == node.parent:
            parent = node.parent
            self.left_rotate(node.parent)
            self.insert_fixup(parent)
            return

        parent.set_black_node()          # node, node.parent, node.parent.parent同边
        grand.set_red_node()
        if parent.left == node and grand.left == node.parent:
            self.right_rotate(grand)
            return
        if parent.right == node and grand.right == node.parent:
            self.left_rotate(grand)
            return

    def add_node(self,node):
        self.action = 'inser node {}.'format(node.val)
        self.insert_node(node)
        self.insert_fixup(node)

        pass
  
    def check_node(self,node):
        '''
        *删除节点是根节点或红色节点，直接删除
        '''
        if self.root == node or node.is_red_node():
            return
        node_is_left = node.parent.left == node
        brother = node.parent.right if node_is_left else node.parent.left
        '''
        *删除节点黑色节点，兄弟节点是红色节点，旋转父节点，节点和兄弟节点都变黑色
        '''
        if brother.is_red_node():
            if node_is_left:
                self.left_rotate(node.parent)
            else:
                self.right_rotate(node.parent)
            node.parent.set_red_node()
            brother.set_black_node()
            print("check node delete more")
            self.check_node(node)
            return
        '''
        *删除黑色节点，兄弟节点也是黑色，且要么没有兄弟节点，要么所有节点都是黑色
        '''
        all_none = noe brother.left and not brother.right
        all_black = brother.left and brother.right and brother.left.is_black_node() and brother.right.is_black_node():
        if all_none or all_black:
            brother.set_red_node()
            if node.parent.is_red_node():
                node.parent.set_black_node()
                return
            self.check_node(node.parent)
            return

        '''
        *检查兄弟节点同则且子节点为红色，
        '''
        brother_same_right_red = node_is_left and brother.right and brother.right.is_red_node()
        brother_same_left_red=not node_is_left and brother.left and brother.left.is_red_node()
        if brother_same_right_red or brother_same_left_red:
            if node.parent.is_red_node():
                brother.set_red_node()
            else:
                brother.set_black_node()
            node.parent.set_black_node()
            if brother_same_right_red:
                brother.right.set_black_node()
                self.left_rotate(node.parent)
            if brothe_sanme_left_red:
                brother.left.set_black_node()
                self.right_totate(node.parent)
            return
        '''
        *检查兄弟节点异则且子节点为红色，
        '''
        borther_diff_right_red=not node_is_left and brother.right and brother.right.is_red_node()
        brother_diff_left_red=node_is_left and brother.left and brother.left.is_red_node()
        if brother_diff_right_red or brother_diff_left_red:
            brother.set_red_node()
            if brother_diff_right_red:
                brother.right.set_black_node()
                self.left_rotate(brother)
            if brother_diff_left_red:
                brother.left.set_black_node()
                self.right_rotate(brother)

            self.check_node(node)
            return
    def pre_delete_node(self,node):
        '''
        *删除前检查，返回要删除的点
        '''
        post_node=self.get_post_node(node)
        if post_node:
            node.val, post_node.val = post_node.val, node.val
            return self.pre_delete_node(post_node)
        pre_node = self.get_pre_node(node)
        if pre_node:
            pre_node.val, node.val = node.val, pre_node.val
            return self.pre_delete_node(pre_node)

        return node
    def get_pre_node(self,node):
        '''前驱节点，比node小的节点中的最大值'''
        if not node.left:
            return None
        pre_node = node.left
        while pre_node.right:
            pre_node = pre_node.right
        return pre_node
    def get_post_node(self,node):
        '''后续节点，比node大的节点中的最小值'''
        if not node.right:
            return None
        post_node = node.right
        while post_node.left:
            post_node = post_node.left
        return post_node
    def get_node(self,val)
        '''根据值查询节点信息'''
        if not self.root:
            return None
        node = self.root
        while node:
            if node.val == val:
                break
            if node.val > val:
                node = node.left
                continue
            else:
                node = node.right
        return node
    def delete_node(self,node):
        if self.root == node:
            self.root = None
            return
        if node.parent.left == node:
            node.parent.left = None
            return
        if node.parent.right == node:
            node.parent.right = None
            return

    if __nama__=='__main__':
        tree = RBTree()
        data = list(range(1,20))
        random.shuffle(data)
        print(data)
        for i in data:
            tree.add_node(RBNode(i))

        random.shuffle(data)
        for i in data:
            print("detele ", i)
            tree.delete_node(i)

    '''
    def tree_log(func):
    @functools.wraps(func)
    def function(a, b):
        save_rb_tree(a.root, "{}-{}".format(a.index, a.action))
        a.index += 1
        func(a, b)
        save_rb_tree(a.root, "{}-{}".format(a.index, a.action))
        a.index += 1

    return function
    
    def delete_node(self, val):

        node = self.get_node(val)
        if not node:
            print("node error {}".format(val))
            return
        save_rb_tree(self.root, "{}_delete_0".format(val))
        # 获取真正要删除的节点
        node = self.pre_delete_node(node)
        save_rb_tree(self.root, "{}_delete_1".format(val))
        # node 节点必不为空，且子节点也都为空
        self.check_delete_node(node)
        save_rb_tree(self.root, "{}_delete_2".format(val))
        #真正删除要删除的节点
        self.real_delete_node(node)
        save_rb_tree(self.root, "{}_delete_3".format(val))
        pass

    '''
        
                
            
        
            
        
 
            
        




                   
