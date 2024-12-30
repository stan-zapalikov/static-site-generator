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
        return markdown_to_heading(block)
    elif re.match(r"^```(?:.|\n)*```$", block):  # Matches fenced code block
        return markdown_to_code(block)
    elif re.match(r"^[-*]\s.*(?:\n.*)*", block):  # Matches unordered list items
        return markdown_to_ul(block)
    elif re.match(r"^\d+\.\s.*(?:\n.*)*", block):  # Matches ordered list items
        return markdown_to_ol(block)
    elif re.match(r"^\s*>.*$", block):  # Matches blockquote lines
        return markdown_to_quote(block)
    else:
        return markdown_to_paragraph(block)
    
def markdown_to_heading(block):
    headingCounter = 0
    for char in block:
        if char != '#':
            break
        headingCounter += 1
    return LeafNode(f"h{headingCounter}", block[headingCounter+1:])

def markdown_to_code(block):
    return ParentNode("pre", [LeafNode("code", block[3:-3])])

def markdown_to_quote(block):
    return LeafNode("blockquote", block[2:])

def markdown_to_paragraph(block):
    return LeafNode("p", block)

def markdown_to_ul(block):
    list_items = block.split("\n")
    html_li = []
    for li in list_items:
        html_li.append(LeafNode("li", li[2:]))
    return ParentNode("ul", html_li)

def markdown_to_ol(block):
    list_items = block.split("\n")
    html_li = []
    for li in list_items:
        html_li.append(LeafNode("li", li[3:]))
    return ParentNode("ol", html_li)
    
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    contents = []
    for block in blocks:
        contents.append(block_to_block_type(block))
    return ParentNode("div", contents)