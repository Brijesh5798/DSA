class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, key):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if key == "both":
            print(prefix + self.name + " (" + self.designation + ")")
        else:
            value = getattr(self, key, None)
            print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(key)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
def build_organization_tree():
    root = TreeNode("Nilupul", "CEO")

    CTO = TreeNode("Chinmay", "CTO")
    IH = TreeNode("Vishwa", "Infrastructure Head")
    CTO.add_child(IH)
    IH.add_child(TreeNode("Dhaval", "Cloud Manager"))
    IH.add_child(TreeNode("Abhijit", "App Manager"))
    CTO.add_child(TreeNode("Amar", "Application Head"))

    HR = TreeNode("Gels", "HR Head")
    HR.add_child(TreeNode("Peter", "Recruitment Manager"))
    HR.add_child(TreeNode("Waqas", "Policy Manager"))

    root.add_child(CTO)
    root.add_child(HR)
    return root
    
if __name__ == '__main__':
    root_node = build_organization_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy