class tree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __add__(self, data):
        if data == self.data:
            return                 # if data is already in data set
        if data <= self.data:
            if self.left:
                self.left.__add__(data)       # recursion function
            else:
                self.left = tree(data)
        else:
            if self.right:
                self.right.__add__(data)      # recursion function
            else:
                self.right = tree(data)

    def in_order(self):
        element = []

        if self.left:
            element += self.left.in_order()     # recursion function

        if self.data:
            element.append(self.data)

        if self.right:
            element += self.right.in_order()     # recursion function

        return element


def build_terr(elements):
    root = tree(elements[0])      # setting root node

    for i in range(len(elements)):
        root.__add__(elements[i])

    return root

numbers = [17, 1, 5, 4, 20, 9, 23, 18, 34, 18, 3]
num_tree = build_terr(numbers)
print(num_tree.in_order())
