import re

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
