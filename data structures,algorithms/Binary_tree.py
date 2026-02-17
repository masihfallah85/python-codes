#Binary_tree.py

"""
In this script we implement a binary tree
"""

class tree:

    """Abstract tree class"""

    class position:

        """A nested class for methods of one node,mainly its elemtn and positon"""

        def element(self):

            """Returns element stored at a node"""

            raise NotImplementedError("must be implemented by subclass")
        
        def __eq__(self,other):
            
            """Checks if positions refer to sme location"""

            raise NotImplementedError("must  be implemented by a sublass")
        
        def __ne__(self,other):
            
            """Checks if positions dont refere to same location"""

            raise NotImplementedError("must be implemented by a subclass")
        
    
    #abstract methods

    def root(self):

        """Returns root of tree"""

        raise NotImplementedError("must be implemented by subclass")
    
    def parrent(self,position):

        """Returns parrent of node at the position"""

        raise NotImplementedError("must be implemented by a subclass")
    
    def number_of_children(self,position):

        """Retunrs number of children of a node at the position """

        raise NotImplementedError("must be implemented by subclass")
    
    def children(self,position):

        """Genrates children foa ndoe at the position """

        raise NotImplementedError("must be implemented by subclass")
    

    def __len__(self):

        """Returns total number of elements in tree"""

        raise NotImplementedError("must be implemented by subclass")
    
    #concrete methods

    def is_root(self,position):

        """Checks if a position is root or not"""

        return self.root() == position
    
    def is_leaf(self,position):

        """Checks if a position is leaf or not"""

        return self.number_of_children(position) == 0
    
    def is_emtpy(self):

        """Checks if tree is empty or not"""

        return len(self) == 0
    
    def depth(self,position):

        """Returns distance of a position and root"""

        if self.is_root(position):

            return 0
        
        return 1 + self.depth(self.parrent(position))
    

    def height(self,position):

        """Returns height of a position"""

        if self.is_leaf(position):

            return 0
        
        return 1 + max(self.height(child) for child in self.children(position))
    

class abstract_binary_tree(tree):

    """Abstract base class representing a binary tree structure"""

    #abstract methods

    def left(self,position):


        """Returns left child of a position"""

        raise NotImplementedError("must be implemented by subclass")

    def right(self, position):

        """Returns right child of a position"""

        raise NotImplementedError("must be implemented by subclass")

    #concrete methods

    def sibling(self, position):

        """Returns siblings of a position"""

        parent = self.parrent(position)

        if parent is None: 
                              
            return None
        
        else:

            if position == self.left(parent):

                return self.right(parent)    
            
            else:

                return self.left(parent)      
            
    def children(self, position):

        results = []

        if self.left(position) is not None:

           results.append(self.left(position))

        if  self.right(position) is not None:

            results.append(self.right(position))

        return results
    
class binary_tree(abstract_binary_tree):

    """Concrete binary tree class"""

    class _node:

        """Node class"""

        __slots__ = "_element", "_parent", "_left", "_right"

        def __init__(self, element, parent=None, left=None, right=None):

            "Node consturctor"

            self._element = element

            self._parent = parent

            self._left = left

            self._right = right

    class Position(abstract_binary_tree.position):


        def __init__(self, container, node):

            "constructor of position class"

            self._container = container

            self._node = node

        def element(self):

            return self._node._element

        def __eq__(self, other):

            return type(other) is type(self) and other._node is self._node
            
        def __ne__(self, other):

            return not (self == other)

    def __init__(self):

        """Binary class constructro"""

        self._root = None

        self._size = 0

    def _validate(self, position):

        """Return associated node, if position is valid"""

        if not isinstance(position, self.Position):

            raise TypeError("position must be proper Position type")
        
        if position._container is not self:

            raise ValueError("position does not belong to this container")
        
        if position._node._parent is position._node:  

            raise ValueError("positon is no longer valid")
        
        
        return position._node
    
    def _make_position(self, node):

        """Return position instance for given node or None if no node"""

        return self.Position(self, node) if node is not None else None

    def __len__(self):

        return self._size

    def root(self):

        return self._make_position(self._root)

    def parrent(self, position):

        node = self._validate(position)

        return self._make_position(node._parent)

    def left(self, position):

        node = self._validate(position)

        return self._make_position(node._left)

    def right(self, position):

        node = self._validate(position)

        return self._make_position(node._right)

    def number_of_children(self, position):

        node = self._validate(position)

        count = 0

        if node._left is not None: count += 1

        if node._right is not None: count += 1

        return count
    
    def add_root(self, element):

        """Place element at root of an empty tree and return new position"""

        if self._root is not None: 
            
            raise ValueError("Root exists")

        self._size = 1

        self._root = self._Node(element)

        return self._make_position(self._root)

    def add_left(self, position, element):

        """create a new left child for position , storing element"""

        node = self._validate(position)

        if node._left is not None: 
            
            raise ValueError("Left child exists")
        
        self._size += 1

        node._left = self._Node(element, node)

        return self._make_position(node._left)

    def add_right(self, position, element):

        """Create a new right child for position , storing element"""

        node = self._validate(position)

        if node._right is not None:
            
            raise ValueError('Right child exists')
        
        self._size += 1

        node._right = self._Node(element, node)

        return self._make_position(node._right)
    
    def replace(self,position,element):

        """Replaces an element inside a position"""

        node = self._validate(position)

        old = node._element

        node._element = element

        return old