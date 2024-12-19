import unittest
from src.main import text_node_to_html_node
from src.textnode import TextNode, TextType
from src.leafnode import LeafNode

class TestMain(unittest.TestCase):
    def testMdToHTMLProper(self):
        text = TextNode("testing", TextType.BOLD, None)
        textToLeaf = text_node_to_html_node(text)
        leaf = LeafNode("b", text.text, None)
        self.assertEqual(repr(leaf), repr(textToLeaf))


if __name__ == '__main__':
    unittest.main()
