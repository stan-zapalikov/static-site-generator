from .htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    # recursive method to return full html tag of the node and its children
    def to_html(self):
        if (not self.tag):
            raise ValueError("Missing tag")
        if (not self.children):
            raise ValueError("Missing children")
        childNodes = ""
        for child in self.children:
            childNodes += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{childNodes}</{self.tag}>"