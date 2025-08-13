import unittest

from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestDelimiter(unittest.TestCase):
    def test_with_bold(self):
        node = TextNode("This is a sentence with **bold** text", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(nodes, [
            TextNode("This is a sentence with ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ])
        node2 = TextNode("This is a sentence which ends in **bold**", TextType.TEXT)
        nodes2 = split_nodes_delimiter([node2], "**", TextType.BOLD)
        self.assertEqual(nodes2, [
            TextNode("This is a sentence which ends in ", TextType.TEXT),
            TextNode("bold", TextType.BOLD)
        ])
        nodes3 = split_nodes_delimiter([node, node2], "**", TextType.BOLD)
        self.assertEqual(nodes3, [
            TextNode("This is a sentence with ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
            TextNode("This is a sentence which ends in ", TextType.TEXT),
            TextNode("bold", TextType.BOLD)
        ])
        node3 = TextNode("This sentence has **bold** text **appearing** twice", TextType.TEXT)
        nodes4 = split_nodes_delimiter([node3], "**", TextType.BOLD)
        self.assertEqual(nodes4, [
            TextNode("This sentence has ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text ", TextType.TEXT),
            TextNode("appearing", TextType.BOLD),
            TextNode(" twice", TextType.TEXT)
        ])

    def test_with_nothing_to_change(self):
        node = TextNode("Clean, formatless text", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(nodes, [node])

        node2 = TextNode("Text that is already bold?!??", TextType.BOLD)
        nodes2 = split_nodes_delimiter([node2], "**", TextType.BOLD)
        self.assertEqual(nodes2, [node2])

    def test_with_italic(self):
        node = TextNode("This is a sentence with _italic_ text", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(nodes, [
            TextNode("This is a sentence with ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
        ])
        node2 = TextNode("This is a sentence which ends in _italics_", TextType.TEXT)
        nodes2 = split_nodes_delimiter([node2], "_", TextType.ITALIC)
        self.assertEqual(nodes2, [
            TextNode("This is a sentence which ends in ", TextType.TEXT),
            TextNode("italics", TextType.ITALIC)
        ])
        node3 = TextNode("This sentence has _italic_ text _appearing_ twice", TextType.TEXT)
        nodes4 = split_nodes_delimiter([node3], "_", TextType.ITALIC)
        self.assertEqual(nodes4, [
            TextNode("This sentence has ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text ", TextType.TEXT),
            TextNode("appearing", TextType.ITALIC),
            TextNode(" twice", TextType.TEXT)
        ])

    def test_with_inline_code(self):
        node = TextNode("In python you can't do `5^2`, instead you do `5**2`", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(nodes, [
            TextNode("In python you can't do ", TextType.TEXT),
            TextNode("5^2", TextType.CODE),
            TextNode(", instead you do ", TextType.TEXT),
            TextNode("5**2", TextType.CODE),
        ])


        


        


if __name__ == "__main__":
    unittest.main()
