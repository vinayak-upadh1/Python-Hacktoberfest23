"""
The diameter/width of a tree is defined as the number of nodes on the longest path
between two end nodes.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    data: int
    left: Node | None = None
    right: Node | None = None

    def depth(self) -> int:
        """
        >>> root = Node(1)
        >>> root.depth()
        1
        >>> root.left = Node(2)
        >>> root.depth()
        2
        >>> root.left.depth()
        1
        >>> root.right = Node(3)
        >>> root.depth()
        2
        """
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return max(left_depth, right_depth) + 1

    def diameter(self) -> int:
        """
        >>> root = Node(1)
        >>> root.diameter()
        1
        >>> root.left = Node(2)
        >>> root.diameter()
        2
        >>> root.left.diameter()
        1
        >>> root.right = Node(3)
        >>> root.diameter()
        3
        """
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return left_depth + right_depth + 1


sys.setrecursionlimit(50000)
# Tree Node


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if(len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size+1

    # Starting from the second element
    i = 1
    while(size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size-1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if(currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size+1
        # For the right child
        i = i+1
        if(i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if(currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size+1
        i = i+1
    return root


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    r"""
    Constructed binary tree is
        1
       / \
      2	  3
     / \
    4	 5
    """
    print(f"{root.diameter() = }")  # 4
    print(f"{root.left.diameter() = }")  # 3
    print(f"{root.right.diameter() = }")  # 1
