from re import I


class Node:
    def __init__(self, val):
        self.left: Node = None
        self.right: Node = None
        self.val = val

    # A function to do inorder tree traversal
    def print_inorder(self, root):
        if root:
            self.print_inorder(root.left)

            print(root.val)

            self.print_inorder(root.right)

    # A function to do preorder tree traversal
    def print_preorder(self, root):
        if root:
            print(root.val)

            self.print_preorder(root.left)

            self.print_preorder(root.right)

    # A function to do postorder tree traversal
    def print_postorder(self, root):
        if root:
            self.print_postorder(root.left)

            self.print_postorder(root.right)

            print(root.val)

    def search(self, root, val):
        # Base Cases: root is null or val is present at root
        if root is None or root.val == val:
            return root

        # val is greater than root's val
        if root.val < val:
            return self.search(root.right, val)

        # val is smaller than root's val
        return self.search(root.left, val)

    def insert(self, root, val):
        if root is None:
            return Node(val)
        else:
            if root.val == val:
                return root
            elif root.val < val:
                root.right = self.insert(root.right, val)
            else:
                root.left = self.insert(root.left, val)
        return root

    #       tree
    #       ----
    #        j    <-- root
    #      /   \
    #     f      k
    #   /   \      \
    #  a     h      z    <-- leaves

    '''
          tree
          ----
            1   
          /   \
         2      3
       /   \     
      4     5     
        
    1) Depth First Traversals: 
        (a) Inorder (Left, Root, Right) : 4 2 5 1 3 
        (b) Preorder (Root, Left, Right) : 1 2 4 5 3 
        (c) Postorder (Left, Right, Root) : 4 5 2 3 1
    
    2) Breadth-First or Level Order Traversal: 1 2 3 4 5 
    '''


def main():
    # create root
    root = Node(1)
    ''' following is the tree after above statement
          1
        /   \
      None  None'''

    root.left = Node(2)
    root.right = Node(3)

    ''' 2 and 3 become left and right children of 1
               1
            /      \
           2          3
        /    \      /   \
      None  None   None None'''

    root.left.left = Node(4)
    '''4 becomes left child of 2
               1
          /         \
          2           3
        /   \       /   \
       4    None  None   None
      /  \
     None None'''

    root.left.right = Node(5)

    print("\nInorder traversal of binary tree is")
    root.print_inorder(root)

    print("Preorder traversal of binary tree is")
    root.print_preorder(root)

    print('Postorder traversal of binary tree is')
    root.print_postorder(root)

    print('\nSearching...')
    root2 = Node(8)
    root2.left = Node(3)
    root2.left.left = Node(1)
    root2.left.right = Node(4)

    root2.right = Node(10)
    root2.right.left = Node(9)
    root2.right.right = Node(15)

    root2.right.right.left = Node(13)
    root2.right.right.right = Node(22)
    print(root2.search(root2, 22))
    print(root2.search(root2, 9))
    print(root2.search(root2, 4))

    print('\nInserting...')
    root3 = Node(50)
    root3.insert(root3, 30)
    root3.insert(root3, 20)
    root3.insert(root3, 40)
    root3.insert(root3, 70)
    root.print_inorder(root3)



if __name__ == '__main__':
    main()
