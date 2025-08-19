from extract_markdown_links import extract_markdown_links, extract_markdown_images
from textnode import TextType, TextNode

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            active_text = node.text
            extracted_stuff = extract_markdown_images(node.text)
            for image in extracted_stuff:
                image_alt, image_link = image[0], image[1]
                sections = active_text.split(f"![{image_alt}]({image_link})", 1)

                if sections[0]:
                    new_nodes.append(TextNode(sections[0],TextType.TEXT))
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))

                if len(sections) == 2:
                    active_text = sections[1]
                else:
                    active_text = None
            if active_text:
                new_nodes.append(TextNode(active_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            active_text = node.text
            extracted_stuff = extract_markdown_links(node.text)
            for link in extracted_stuff:
                clicky_text, url = link[0], link[1]
                sections = active_text.split(f"[{clicky_text}]({url})", 1)

                if sections[0]:
                    new_nodes.append(TextNode(sections[0],TextType.TEXT))
                new_nodes.append(TextNode(clicky_text, TextType.LINK, url))
                
                if len(sections) == 2:
                    active_text = sections[1]
                else: active_text = "" 
            if active_text:
                new_nodes.append(TextNode(active_text, TextType.TEXT))

    return new_nodes
