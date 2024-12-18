import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def testPropsToHtml(self):
        node = HTMLNode("","",[], {"href":"google", "color": 70310})
        self.assertEqual(node.props_to_html(), " href=\"google\" color=\"70310\"")

    def testRepr(self):
        node = HTMLNode("", "", [], {})
        node2 = HTMLNode("", "", [], {})
        self.assertEqual(repr(node), repr(node2))

if __name__ == '__main__':
    unittest.main()
