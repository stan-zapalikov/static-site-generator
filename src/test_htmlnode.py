import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def testPropsToHtml(self):
        node = HTMLNode("","",[], {"href":"google", "color": 70310})
        self.assertEqual(node.props_to_html(), " href=\"google\" color=\"70310\"")

    def testRepr(self):
        node = HTMLNode("", "", [], {})
        node2 = HTMLNode("", "", [], {})
        self.assertEqual(repr(node), repr(node2))

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
