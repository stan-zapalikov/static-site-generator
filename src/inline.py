import re
from .textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if (node.text_type != TextType.TEXT):
            new_nodes.append(node)
            continue
        start = node.text.find(delimiter)
        if (start != -1):
            end = node.text.find(delimiter, start + 1)
            if (end != -1):
                new_nodes.append(TextNode(node.text[:start], TextType.TEXT))
                new_nodes.append(TextNode(node.text[start+1:end], text_type))
                new_nodes.append(TextNode(node.text[end+1:], TextType.TEXT))
            else:
                new_nodes.append(node)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    pass

def split_nodes_link(old_nodes):
    pass
        

