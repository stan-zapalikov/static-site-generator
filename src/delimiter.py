from .textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if (node.text_type != TextType.TEXT):
            new_nodes.append(node)
        else:
            split_node = node.split(delimiter)
            if (len(split_node) != 3):
                raise Exception("Invalid markdown syntax")
            split_node[1].text_type = text_type
            new_nodes.extend(split_node)

    return new_nodes
