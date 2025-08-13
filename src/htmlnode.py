from textnode import TextType

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        NotImplementedError()

    def props_to_html(self):
        string = ""
        for key in self.props:
            string += f' {key}="{self.props[key]}"'
        return string

    def __repr__(self):
        print(f"tag is {self.tag}, value is {self.value}, children are {self.childern} & props are {self.props}")


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props, children=None)

    def to_html(self):
        if not self.value:
            raise ValueError("Lead nodes must have a value")
        elif not self.tag:
            return self.value
        else:
            if not self.props:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                string = f"<{self.tag} "
                for key in self.props:
                    string += f'{key}="{self.props[key]}"'
                string += f">{self.value}</{self.tag}>"
                return string
        

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, props=props, children=children)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        elif not self.children:
            raise ValueError("ParentNode must have children")
        else:
            string = f"<{self.tag}>"
            for child in self.children:
                string += child.to_html()
            return string + f"</{self.tag}>"


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception("Invalid text type")

        

