import unittest
from src.delimiter import split_nodes_delimiter
from src.textnode import TextNode, TextType

class TestDelimiter(unittest.TestCase):
    def testProperWithOneNode(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        convertedSubnodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]

    def testIncompleteWithOneNode(self):
        node = TextNode("This is text with a code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertRaises(Exception);

    def testProperWithTwoNodes(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        convertedSubnodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, convertedSubnodes)


if __name__=='__main__':
    unittest.main()
