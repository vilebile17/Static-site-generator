from markdown_to_textnodes import text_to_textnodes, markdown_to_blocks
from blocktypes import BlockType, block_to_block_type 
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType
from markdown_to_textnodes import text_to_textnodes

def markdown_to_html_node(markdown):
    block_list = markdown_to_blocks(markdown)
    parent_list = []
    for block in block_list:
        its_type = block_to_block_type(block)
        new_nodes = []

        hashcount = 0
        if its_type == BlockType.HEADING:
            hashcount = count_hashtags(block)
            block = block.split(" ", 1)[1]
            new_nodes = text_to_children(block)

        elif its_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            for line in lines:
                line = line.split(". ", 1)[1]
                if not text_to_children(line):
                    new_nodes.append(LeafNode("li", line))
                else:
                    new_nodes.append(ParentNode("li", text_to_children(line)))

        elif its_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            for line in lines:
                line = line.split("- ", 1)[1]
                if not text_to_children(line):
                    new_nodes.append(LeafNode("li", line))
                else:
                    new_nodes.append(ParentNode("li", text_to_children(line)))
            
        elif its_type == BlockType.PARAGRAPH:
            new_nodes = text_to_children(block.replace("\n", " "))

        elif its_type == BlockType.QUOTE:
            lines = block.split("\n")
            new_lines = []
            for line in lines:
                new_lines.append(line[1:])
            for line in new_lines:
                if not text_to_children(line):
                    new_nodes.append(LeafNode("p", line))
                else:
                    new_nodes.append(ParentNode("p", text_to_children(line)))

        elif its_type == BlockType.CODE:
            text_node = TextNode(extract_code(block), TextType.CODE) # a code block should just be one massive block
            parent_node = ParentNode("pre", [text_node_to_html_node(text_node)]) 
           
        if its_type != BlockType.CODE:
            parent_node = ParentNode(get_parent_tag(its_type,hashcount), new_nodes)

        parent_list.append(parent_node)
    
    grandest_parent = ParentNode("div", parent_list)
    return grandest_parent
        

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    html_kids = []
    for textnode in textnodes:
        html_kids.append(text_node_to_html_node(textnode))
    return html_kids

def get_parent_tag(text_type, hashes=0):
    if text_type == BlockType.QUOTE:
        return "blockquote"
    elif text_type == BlockType.UNORDERED_LIST:
        return "ul"
    elif text_type == BlockType.ORDERED_LIST:
        return "ol"
    elif text_type == BlockType.CODE:
        return "code"
    elif text_type == BlockType.HEADING:
        return f"h{hashes}"
    else:
        return "p"

def count_hashtags(line):
    counter = 0
    while True:
        if counter >= 6:
            return 6
        elif line[counter] == "#":
            counter += 1
        else:
            return counter

def extract_code(block):
    code = block.split("```\n", 1)[1]
    return code.split("```", 1)[0]



md = """
# Hi there!

This is some _italic_ text

- an item with **bold text**
- an item with `inline code`

> A very **wise** quote
> A second _wise_ quote

1. first **bold** item
2. second _italic_ item
3. third `code` item

```
print("hello world")
print("boo")
```
"""
