import unittest

from src.textnode import TextNode, TextType
from src.leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def testEq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def testTextEq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is NOT a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def testTypeEq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def testURLEq(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://google.com/")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def testMdToHTMLProper(self):
        text = TextNode("testing", TextType.BOLD, None)
        textToLeaf = text.text_node_to_html_node()
        leaf = LeafNode("b", text.text, None)
        self.assertEqual(repr(leaf), repr(textToLeaf))


if __name__ == '__main__':
    unittest.main()
