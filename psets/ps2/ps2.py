class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: int
    # item: int
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
         return self._size
       
     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Part a #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    '''
    def select(self, ind):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        if ind == left_size:
            return self
        if left_size > ind and self.left is not None:
            return self.left.select(ind)
        if left_size < ind and self.right is not None: 
            return self.right.select(ind-left_size-1) #!! 
        return None


    #The correctness issue with select was that the logic was broken when traversing to the right child node
    #When you go to the left child node, it's because the current node's index is too large, 
    #so you definitely don't need to consider the nodes on the right of the current node. So keeping the same ind value
    #works
    #when you go to the right node, that means the current node's index is too small, 
    #but on the right node, you lose all the previous context of the nodes that were smaller than it, 
    #including the previous node and its left children. so you need to adjust the target index to account
    #for the fact that those smaller indexes are no longer counted by left_size. 
    #You do this by subtracting left_size and 1, so that ind is relevant to the subtree of the right node


    #if coming from the right, index of a node = parent's index + 1 + size left
    #if coming from the left, index of a node = parent's index - 1 - size right
    #if first node, index of node = left child + 1
    #^the above is scratch notes i took describing the absolute index of a given node, and is not what I implemented
    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    def search(self, key):
        if self is None:
            return None
        elif self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None
    

    '''
    Inserts a key into the tree
    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    '''
    #insert ran in at least linear time because of the unnecessary call to calculate_sizes(). 
    #this recalculates every single size of every node in the tree, which is at least O(n)
    #This can be fixed by simply adding 1 to the size of every node touched, since you know that 
    #you will only be adding one node to the tree. This is an O(1) operation when done alongside 
    #all the other operations. 
    def insert(self, key):
        if self.key is None:
            self.key = key
            self.size=0
        elif self.key > key: 
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.left.insert(key)
        elif self.key < key:
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
            self.right.insert(key)
        #self.calculate_sizes()
        self.size+=1
        return self
