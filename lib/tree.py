class Tree:
    def __init__(self, root):
        self.root = root  # A dict with keys like 'id', 'tag_name', 'text_content', 'children'

    def get_element_by_id(self, target_id):
        def traverse(node):
            if node.get('id') == target_id:
                return node
            for child in node.get('children', []):
                result = traverse(child)
                if result:
                    return result
            return None

        return traverse(self.root)
