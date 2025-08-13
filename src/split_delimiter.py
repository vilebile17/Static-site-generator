from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            new_texts = node.text.split(delimiter)
            if len(new_texts) == 2:
                raise ValueError(f"No matching {delimiter} was found for node {node}")

            for i in range(len(new_texts)): # loops over every new piece of text made
                if new_texts[i]:
                    if i % 2 == 0:
                        new_nodes.append(TextNode(new_texts[i], TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(new_texts[i], text_type))

    return new_nodes
