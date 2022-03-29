def print_tree_diagram(root, val="val", left="left", right="right"):
    def display(root, val=val, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, val, left, right)
    for line in lines:
        print(line)


# A function to do inorder tree traversal
def print_inorder(root):
    if root:
        print_inorder(root.left)

        print(root.val)

        print_inorder(root.right)


# A function to do preorder tree traversal
def print_preorder(root):
    if root:
        print(root.val)

        print_preorder(root.left)

        print_preorder(root.right)


# A function to do postorder tree traversal
def print_postorder(root):
    if root:
        print_postorder(root.left)

        print_postorder(root.right)

        print(root.val)


def search(root, val):
    # Base Cases: root is null or val is present at root
    if root is None or root.val == val:
        return root

    # val is greater than root's val
    if root.val < val:
        return search(root.right, val)

    # val is smaller than root's val
    return search(root.left, val)

def minValueNode(node):
    current = node
 
    # loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left
 
    return current
 

def delete(root,val):
    if root is None:
        return root
    
    # If the val to be deleted
    # is smaller than the root's
    # val then it lies in  left subtree
    if val < root.val:
        root.left = delete(root.left,val)
    
    # If the val to be delete
    # is greater than the root's val
    # then it lies in right subtree
    elif(val > root.val):
        root.right = delete(root.right, val)
    
    # If val is same as root's val, then this is the node
    # to be deleted
    else:
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
 
        elif root.right is None:
            temp = root.left
            root = None
            return temp
 
        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)
 
        # Copy the inorder successor's
        # content to this node
        root.val = temp.val
 
        # Delete the inorder successor
        root.right = delete(root.right, temp.val)
 
    return root
    

def insert(root, val):
    if root is None:
        return Node(val)
    else:
        if root.val == val:
            return root
        elif root.val < val:
            root.right = insert(root.right, val)
        else:
            root.left = insert(root.left, val)
    return root

class Node:
    def __init__(self, val):
        self.left: Node = None
        self.right: Node = None
        self.val = val

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
    print_inorder(root)

    print("Preorder traversal of binary tree is")
    print_preorder(root)

    print('Postorder traversal of binary tree is')
    print_postorder(root)

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
    print(search(root2, 22))
    print(search(root2, 9))
    print(search(root2, 4))

    print('\nInserting...')
    root3 = Node(5)
    insert(root3, 4)
    insert(root3, 2)
    insert(root3, 3)
    insert(root3, 1)
    insert(root3, 7)
    insert(root3, 11)
    insert(root3, 6)
    print_tree_diagram(root3)

    print('\nDeleting...')
    delete(root3, 4)
    delete(root3, 5)
    print_tree_diagram(root3)
      


if __name__ == '__main__':
    main()
