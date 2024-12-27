import unittest
from src.inline import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
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


    def testMdImages(self):
        text = "This is text with a ![img1](https://i.imgur.com/aKaOqIh.gif) and ![img2](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = [("img1", "https://i.imgur.com/aKaOqIh.gif"), ("img2", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text), result)

    def testMdText(self):
        text = "This is text with a link [to google](https://www.google.com) and [to youtube](https://www.youtube.com/)"
        result = [("to google", "https://www.google.com"), ("to youtube", "https://www.youtube.com/")]
        self.assertEqual(extract_markdown_links(text), result)


if __name__=='__main__':
    unittest.main()
