"""Binary Tree:A node can have maximum two children
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)
n6=Node(60)
n7=Node(70)
n1.left=n2
n1.right=n2
n2.left=n4
n4.right=n5
n3.left=n6
n3.right=n7





class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key
# A function to do inorder tree traversal :left->root->right
def printInorder(root):
	if root:
		# First recur on left child
		printInorder(root.left)
		# then print the data of node
		print(root.val)
		# now recur on right child
		printInorder(root.right)
# Driver code
if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	# Function call
	print("\nInorder traversal of binary tree is")
	printInorder(root)




# A class that represents an individual node in a
# Binary Tree


class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# A function to do preorder tree traversal :root->left->right
def printPreorder(root):

	if root:

		# First print the data of node
		print(root.val)

		# Then recur on left child
		printPreorder(root.left)

		# Finally recur on right child
		printPreorder(root.right)






        
# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

# Function call
print("Preorder traversal of binary tree is")
printPreorder(root)


# Python3 program to for tree traversals

# A class that represents an individual node in a
# Binary Tree


class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

# A function to do postorder tree traversal :left->right->root
def printPostorder(root):
	if root:

		# First recur on left child
		printPostorder(root.left)

		# the recur on right child
		printPostorder(root.right)

		# now print the data of node
		print(root.val)


# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

# Function call
print("\nPostorder traversal of binary tree is")
printPostorder(root)

#Types of binary tree:
    #Full  binary tree:Every nodes will have zero or two children
    #Pathalogical tyree:Every nodes will have zero or one children
    #complete binary tree:1.Every level should be full or complete (have extreme left and right)
                         #2.In last level if it is incomplete nodes should present at extreme left side
    #Perfect binary tree:all internal nodes which has two children and leaf nodes should be at same level
    #BAlanced tree:For all the nodes Height(left subtree)-Height(right subtree) can be 0 or 1
    #Binary Search tree:left side of root should be less thsn root right side should be greater then root
#80 10 15 16 45 0 92 73 44
#200 25 5 10 15 -10 -30 61 97 -88 -55 77
#54321 12345 -1 -2 -3 -4 -5 0

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)
n6=Node(60)
n7=Node(70)
n1.left=n2
n1.right=n2
n2.left=n4
n4.right=n5
n3.left=n6
n3.right=n7
"""

#implementation or insertion  of BST
 
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val=key
def insert(root, key):
    if  root is None:
        return  Node(key)
    else:
        if root.val==key:
            return root
        elif root.val<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root      

# Function to display the output of the tree
def display(root):
    if root:
        display(root.left)
        print(root.val)
        display(root.right)

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

display(r)

#Deletion in BST
# Python program to demonstrate delete operation
# in binary search tree

# A Binary Tree Node


class Node:

	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


# A utility function to do inorder traversal of BST
def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.key, end=" ")
		inorder(root.right)


# A utility function to insert a
# new node with given key in BST
def insert(node, key):

	# If the tree is empty, return a new node
	if node is None:
		return Node(key)

	# Otherwise recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)

	# return the (unchanged) node pointer
	return node

# Given a non-empty binary
# search tree, return the node
# with minimum key value
# found in that tree. Note that the
# entire tree does not need to be searched


def minValueNode(node):
	current = node

	# loop down to find the leftmost leaf
	while(current.left is not None):
		current = current.left

	return current

# Given a binary search tree and a key, this function
# delete the key and returns the new root


def deleteNode(root, key):

	# Base Case
	if root is None:
		return root

	# If the key to be deleted
	# is smaller than the root's
	# key then it lies in left subtree
	if key < root.key:
		root.left = deleteNode(root.left, key)

	# If the kye to be delete
	# is greater than the root's key
	# then it lies in right subtree
	elif(key > root.key):
		root.right = deleteNode(root.right, key)

	# If key is same as root's key, then this is the node
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
		root.key = temp.key

		# Delete the inorder successor
		root.right = deleteNode(root.right, temp.key)

	return root


# Driver code
""" Let us create following BST
			50
		/	 \
		30	 70
		/ \ / \
	20 40 60 80 """

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Inorder traversal of the given tree")
inorder(root)

print("\nDelete 20")
root = deleteNode(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 30")
root = deleteNode(root, 30)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 50")
root = deleteNode(root, 50)
print("Inorder traversal of the modified tree")
inorder(root)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

