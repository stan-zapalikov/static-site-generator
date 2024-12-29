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
        self.assertEqual(block_to_block_type(text), "paragraph")

    def testBlockToBlockTypeHeading(self):
        text = "## This is a heading"
        self.assertEqual(block_to_block_type(text), "heading")
        
    def testBlockToBlockTypeUl(self):
        # Each list item should be separate; adjust input to test individual items
        text = "- List item"
        self.assertEqual(block_to_block_type(text), "unordered_list")

    def testBlockToBlockTypeOl(self):
        # Each list item should be separate; adjust input to test individual items
        text = "1. List item"
        self.assertEqual(block_to_block_type(text), "ordered_list")
        
    def testBlockToBlockTypeCode(self):
        text = "```\nthis is code\nthis is more code\n```"
        self.assertEqual(block_to_block_type(text), "code")
        
    def testBlockToBlockTypeQuote(self):
        text = "> This is a quote"
        self.assertEqual(block_to_block_type(text), "quote")

    def testMarkdownToHeading1(self):
        self.assertEqual(repr(markdown_to_heading("# Test")), repr(LeafNode("h1", "Test")))
    
    def testMarkdownToCode(self):
        #tbd
        pass
        


if __name__ == '__main__':
    unittest.main()
