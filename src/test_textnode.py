import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def testEq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def testTextEq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is NOT a text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

    def testTypeEq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.LINK_TEXT)
        self.assertNotEqual(node, node2)

    def testURLEq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, "https://google.com/")
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)



if __name__ == '__main__':
    unittest.main()
