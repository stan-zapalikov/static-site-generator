import re
from .parentnode import ParentNode
from .leafnode import LeafNode

def markdown_to_blocks(text):
    tempBlocks = text.split("\n\n")
    finalBlocks = []
    for block in tempBlocks:
        if (len(block) == 0):
            continue
        finalBlocks.append(block.strip())
    return finalBlocks


def block_to_block_type(block):
    block = block.strip()
    if re.match(r"^#{1,6} .*$", block):  # Matches headings (1-6 `#` characters)
        return "heading"
    elif re.match(r"^```(?:.|\n)*```$", block):  # Matches fenced code block
        return "code"
    elif re.match(r"^\s*[-*]\s.*$", block):  # Matches unordered list items
        return "unordered_list"
    elif re.match(r"^\s*\d+\.\s.*$", block):  # Matches ordered list items
        return "ordered_list"
    elif re.match(r"^\s*>.*$", block):  # Matches blockquote lines
        return "quote"
    else:
        return "paragraph"
    
def markdown_to_heading(block):
    headingCounter = 0
    for char in block:
        if char != '#':
            break
        headingCounter += 1
    return LeafNode(f"h{headingCounter}", block[headingCounter-1:])

def markdown_to_code(block):
    return ParentNode("pre", [LeafNode("code", block[3:-3])])

def markdown_to_quote(block):
    return LeafNode("blockquote", block[2:])

def markdown_to_paragraph(block):
    return LeafNode("p", block)


def markdown_to_html_node(markdown):
    pass