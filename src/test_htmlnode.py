import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag=None,value="skibidi",children="nope",props=None)
        node1 = HTMLNode(tag="<p>",value="not fun",children="Yahya",props={"href": "boot.dev", "target": "_blank"})
        node2 = HTMLNode(tag=None,value="water",children=None,props={"your mum": "The backrooms"})
        self.assertNotEqual(node, node1)
        self.assertNotEqual(node2, node1)
        self.assertNotEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node2 = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')
        node3 = LeafNode(None, "I'm just blank text")
        self.assertEqual(node3.to_html(), "I'm just blank text")


class TestHTMLParentNodes(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("p", "chungus")
        parent_node = ParentNode("div", [child_node])
        parent_node2 = ParentNode("div", [child_node, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
        self.assertEqual(parent_node2.to_html(), "<div><span>child</span><p>chungus</p></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_no_children(self):
        with self.assertRaises(ValueError) as context:
            parent = ParentNode("div", None)
            parent.to_html()
        self.assertEqual(str(context.exception), "ParentNode must have children")


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

        node2 = TextNode("BIG FAT CHUNGUS", TextType.IMAGE, "chungus.png")
        html_node2 = text_node_to_html_node(node2)
        self.assertEqual(html_node2.tag, "img")
        self.assertNotEqual(html_node2.value, "BIG FAT CHUNGUS")
        self.assertEqual(html_node2.props["alt"], "BIG FAT CHUNGUS")
        self.assertEqual(html_node2.props["src"], "chungus.png")

        node3 = TextNode("This is bold text", TextType.BOLD)
        html_node3 = text_node_to_html_node(node3)
        self.assertEqual(html_node3.tag, "b")
        self.assertNotEqual(html_node3.props, {"src": "bold.jpeg"})


if __name__ == "__main__":
    unittest.main()
