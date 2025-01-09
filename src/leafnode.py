from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag is None:
            if self.value is None:
                raise ValueError("Invalid HTML: No value")
            return self.value

        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()}>"
        else:
            if self.value is None:
                raise ValueError("Invalid HTML: No value")
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
