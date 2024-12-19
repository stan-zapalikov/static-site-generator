import unittest
from src.parentnode import ParentNode
from src.leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def testNothingMissing(self):
        childNodes = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text")
        ]
        correct = "<p color=\"blue\" id=\"34\"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        parent = ParentNode("p", childNodes, {"color": "blue", "id": 34})
        self.assertEqual(parent.to_html(), correct)

    def testMissingProps(self):
        childNodes = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text")
        ]
        correct = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        parent = ParentNode("p", childNodes, None)
        self.assertEqual(parent.to_html(), correct)

if __name__ == '__main__':
    unittest.main()
