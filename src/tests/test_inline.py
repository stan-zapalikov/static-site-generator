import unittest
from src.inline import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
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

    def testLinkSplit(self):
        node = TextNode(
            "This is text with a link [google](https://www.google.com) and [to youtube](https://www.youtube.com/)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        result = [
            TextNode("This is text with a link ", TextType.TEXT), 
            TextNode("google", TextType.LINK, "https://www.google.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/"),
        ]
        self.assertEqual(new_nodes, result)

    def testImgSplit(self):
        node = TextNode(
            "This is text with a link ![google](https://www.google.com) and ![to youtube](https://www.youtube.com/)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        result = [
            TextNode("This is text with a link ", TextType.TEXT), 
            TextNode("google", TextType.IMAGE, "https://www.google.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/"),
        ]
        self.assertEqual(new_nodes, result)

    def testTextToTextnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://imgur.com/) and a [link](https://google.com)"
        textNodes = text_to_textnodes(text)
        result = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://imgur.com/"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://google.com"),
        ]
        self.assertEqual(textNodes, result)



if __name__=='__main__':
    unittest.main()
