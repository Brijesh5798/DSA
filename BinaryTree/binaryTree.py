class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()
            
        elements.append(self.data)

        return elements
    
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            # min_val = self.right.min()
            max_val = self.left.max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self
    
    def min(self):
        if self.left != None:
            return self.left.min()
        return self.data
    
    def max(self):
        if self.right != None:
            return self.right.max()
        return self.data
    
    def sum(self):
        left_sum = self.left.sum() if self.left else 0
        right_sum = self.right.sum() if self.right else 0
        return self.data + left_sum + right_sum

def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    print("MIN",numbers_tree.min())
    print("MAX",numbers_tree.max())
    print("Sum",numbers_tree.sum())
    print("Post order traversal gives this sorted list:",numbers_tree.post_order_traversal())
    print("Pre order traversal gives this sorted list:",numbers_tree.pre_order_traversal())
    numbers_tree.delete(20)
    print("After deleting 20 ",numbers_tree.in_order_traversal()) # this should print [1, 4, 9, 17, 18, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(9)
    print("After deleting 9 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 17, 18, 20, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(17)
    print("After deleting 17 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 9, 18, 20, 23, 34]
    