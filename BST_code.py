class BinarySearchTree:
    def __init__(self,values):
        self.values = values

    def get_left_child_index(self,parent_index):
         return ( 2 * parent_index + 1)

    def get_right_child_index(self,parent_index):
        return ( 2 * parent_index + 2)

    def get_parent_index(self,child_index):
        return (child_index - 1 // 2)
    

BST_as_list= [15,9,22,4,12,17,29]
bst = BinarySearchTree(BST_as_list)
index = 0
parent_index = bst.get_parent_index(index)
left_index = bst.get_left_child_index(index)
right_index = bst.get_right_child_index(index)
print(f'parent is at index {parent_index}, value: {BST_as_list[parent_index]}')
print(f'left child is at index {left_index}, value: {BST_as_list[left_index]}')
print(f'right child is at index {right_index}, value: {BST_as_list[right_index]}')
