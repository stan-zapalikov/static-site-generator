import unittest
from src.block import *
from src.parentnode import ParentNode
from src.textnode import TextNode

class TestMarkdownConversion(unittest.TestCase):

    def test_markdown_to_blocks(self):
        text = """# Heading 1

Paragraph text

- List item 1
- List item 2

> Blockquote"""
        expected = ["# Heading 1", "Paragraph text", "- List item 1\n- List item 2", "> Blockquote"]
        self.assertEqual(markdown_to_blocks(text), expected)

    def test_block_to_block_type_heading(self):
        block = "# Heading 1"
        result = block_to_block_type(block)
        self.assertEqual(result.tag, "h1")

    def test_block_to_block_type_code(self):
        block = "```\ncode block\n```"
        result = block_to_block_type(block)
        self.assertEqual(result.tag, "pre")

    def test_block_to_block_type_quote(self):
        block = "> Quote text"
        result = block_to_block_type(block)
        self.assertEqual(result.tag, "blockquote")

    def test_block_to_block_type_paragraph(self):
        block = "This is a paragraph."
        result = block_to_block_type(block)
        self.assertEqual(result.tag, "p")

    def test_markdown_to_heading(self):
        block = "### Heading 3"
        result = markdown_to_heading(block)
        self.assertEqual(result.tag, "h3")

    def test_markdown_to_code(self):
        block = "```code block```"
        result = markdown_to_code(block)
        self.assertEqual(result.tag, "pre")

    def test_markdown_to_quote(self):
        block = "> Blockquote text"
        result = markdown_to_quote(block)
        self.assertEqual(result.tag, "blockquote")

    def test_markdown_to_paragraph(self):
        block = "Paragraph text"
        result = markdown_to_paragraph(block)
        self.assertEqual(result.tag, "p")

    def test_markdown_to_ul(self):
        block = "- List item 1\n- List item 2"
        result = markdown_to_ul(block)
        self.assertEqual(result.tag, "ul")

    def test_markdown_to_ol(self):
        block = "1. Ordered item 1\n2. Ordered item 2"
        result = markdown_to_ol(block)
        self.assertEqual(result.tag, "ol")

    def test_markdown_to_html_node(self):
        markdown = """# Heading 1

Paragraph text

- List item 1
- List item 2"""
        result = markdown_to_html_node(markdown)
        self.assertEqual(result.tag, "div")

    def test_invalid_heading_level(self):
        block = "####### Too many hashes"
        with self.assertRaises(ValueError):
            markdown_to_heading(block)

if __name__ == "__main__":
    unittest.main()
