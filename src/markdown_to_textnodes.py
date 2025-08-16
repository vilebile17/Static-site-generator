from split_delimiter import split_nodes_delimiter
from split_nodes import split_nodes_link, split_nodes_image
from textnode import TextNode, TextType

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT) 
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_link(new_nodes)
    new_nodes = split_nodes_image(new_nodes)
    return new_nodes

def markdown_to_blocks(markdown):
    lst = markdown.split("\n\n")
    for i in range(len(lst)):
        if not lst[i]:
            lst.remove(lst[i])
        else:
            lst[i] = lst[i].strip()
    return lst
