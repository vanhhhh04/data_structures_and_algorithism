class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        spaces = " "* self.get_level()
        print(spaces + self.data)
        if self.children :
            for child in self.children:
                child.print_tree()

    def get_level(self):
        p = self.parent
        level = 0
        while p :
            level += 1
            p = p.parent
        return level


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))


    cellphone = TreeNode("Cellphone")
    cellphone.add_child(TreeNode("Iphone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("Tivi")
    tv.add_child(TreeNode("SamSung"))
    tv.add_child(TreeNode("LG"))


    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()
if __name__=="__main__":
    build_product_tree()
