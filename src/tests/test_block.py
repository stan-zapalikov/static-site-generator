import unittest
from src.block import *

class TestBlock(unittest.TestCase):
    def testMdToBlockProper(self):
        text = "# heading\n\nParagraph\n\n* list\n* list"
        blocks = markdown_to_blocks(text)
        result = ["# heading", "Paragraph", "* list\n* list"]
        self.assertEqual(blocks, result)

    def testMdToBlockExtraSpaces(self):
        text = "# heading\n\n\n\n   Paragraph\n\n\n* list\n* list"
        blocks = markdown_to_blocks(text)
        result = ["# heading", "Paragraph", "* list\n* list"]
        self.assertEqual(blocks, result)


    def testBlockToBlockTypeParagraph(self):
        text = "this is a paragraph"
        self.assertEqual(repr(block_to_block_type(text)), repr(LeafNode("p", "this is a paragraph")))

    def testBlockToBlockTypeHeading(self):
        text = "## This is a heading"
        self.assertEqual(repr(block_to_block_type(text)), repr(LeafNode("h2", "This is a heading")))
        
    def testBlockToBlockTypeUl(self):
        # Each list item should be separate; adjust input to test individual items
        text = "- List item"
        self.assertEqual(repr(block_to_block_type(text)), repr(ParentNode("ul", [LeafNode("li", "List item")])))

    def testBlockToBlockTypeOl(self):
        # Each list item should be separate; adjust input to test individual items
        text = "1. List item\n2. List item2"
        self.assertEqual(repr(block_to_block_type(text)), repr(ParentNode("ol", [LeafNode("li", "List item"), LeafNode("li", "List item2")])))
        
    def testBlockToBlockTypeCode(self):
        text = "```\nthis is code\nthis is more code\n```"
        self.assertEqual(repr(block_to_block_type(text)), repr(ParentNode("pre", [LeafNode("code", "\nthis is code\nthis is more code\n")])))
        
    def testBlockToBlockTypeQuote(self):
        text = "> This is a quote"
        self.assertEqual(repr(block_to_block_type(text)), repr(LeafNode("blockquote", "This is a quote")))


    def testMarkdownToHeading1(self):
        self.assertEqual(repr(markdown_to_heading("# Test")), repr(LeafNode("h1", "Test")))
    
    def testMarkdownToCode(self):
        result = ParentNode("pre", [LeafNode("code", "testing")])
        self.assertEqual(repr(result), repr(markdown_to_code("```testing```")))
        
    def testMarkdownToParagraph(self):
        result = LeafNode("p", "Testing")
        self.assertEqual(repr(result), repr(markdown_to_paragraph("Testing")))
    
    def testMarkdownToQuote(self):
        result = LeafNode("blockquote", "This is a quote")
        self.assertEqual(repr(result), repr(markdown_to_quote("> This is a quote")))

    def testMarkdownToUl(self):
        children = [LeafNode("li", "Testing1"), LeafNode("li", "Testing2")]
        result = ParentNode("ul", children)
        prompt = "* Testing1\n* Testing2"
        self.assertEqual(repr(result), repr(markdown_to_ul(prompt)))

    def testBlockToBlockTypeOl(self):
        text = "1. List item\n2. List item2"
        expected = ParentNode("ol", [
            LeafNode("li", "List item"),
            LeafNode("li", "List item2")
        ])
        self.assertEqual(repr(block_to_block_type(text)), repr(expected))


    def testMarkdownToOlToHtml(self):
        children = [LeafNode("li", "Testing1"), LeafNode("li", "Testing2")]
        result = ParentNode("ol", children)
        prompt = "1. Testing1\n2. Testing2"
        self.assertEqual(result.to_html(), markdown_to_ol(prompt).to_html())

    def testMarkdownToHtmlNodeRepr(self):
        result = "<div><ul><li>Testing1</li><li>Testing2</li></ul></div>"
        markdown = "* Testing1\n* Testing2"
        children = [LeafNode("li", "Testing1"), LeafNode("li", "Testing2")]
        parent = ParentNode("ul", children)
        self.assertEqual(repr(ParentNode("div", [parent])), repr(markdown_to_html_node(markdown)))

    def testMarkdownToHtmlNodeToHtml(self):
        result = "<div><ol><li>Testing1</li><li>Testing2</li></ol></div>"
        markdown = "1. Testing1\n2. Testing2"
        children = [LeafNode("li", "Testing1"), LeafNode("li", "Testing2")]
        parent = ParentNode("ol", children)
        self.assertEqual(result, markdown_to_html_node(markdown).to_html())
    


if __name__ == '__main__':
    unittest.main()
