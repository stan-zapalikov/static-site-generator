from enum import Enum
class TextType(Enum):
    NORMAL_TEXT = "normal"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK_TEXT = "link"
    IMAGE_TEXT = "image"

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
