from enum import Enum
from leafnode import LeafNode
class TextType(Enum):
    TEXT = "TEXT"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, rhs):
        return (
            self.text == rhs.text and
            self.text_type == rhs.text_type and
            self.url == rhs.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


    def text_node_to_html_node(self):
        match (self.text_type):
            case TextType.TEXT:
                return LeafNode(None, self.text, None)
            case TextType.BOLD:
                return LeafNode("b", self.text, None)
            case TextType.ITALIC:
                return LeafNode("i", self.text, None)
            case TextType.CODE:
                return LeafNode("code", self.text, None)
            case TextType.LINK:
                return LeafNode("a", self.text, {"href": self.url})
            case TextType.IMAGE:
                return LeafNode("img", None, {"src": self.url, "alt": self.text})
            case _:
                raise ValueError("Unknown text type")
