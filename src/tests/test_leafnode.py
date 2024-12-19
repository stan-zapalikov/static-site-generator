import unittest
from src.leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def testLeafToHtml(self):
        node = LeafNode("p", "Test", {"href":"link.com"})
        correctResult = "<p href=\"link.com\">Test</p>"
        self.assertEqual(node.to_html(), correctResult)

    def testLeafRepr(self):
        node = LeafNode("p", "Test", {"href":"link.com"})
        correctResult = "HTMLNode(p, Test, None, {\'href\': \'link.com\'})"
        self.assertEqual(repr(node), correctResult)

if __name__ == '__main__':
    unittest.main()
