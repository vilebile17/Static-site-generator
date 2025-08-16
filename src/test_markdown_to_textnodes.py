import unittest

from textnode import TextNode, TextType
from markdown_to_textnodes import text_to_textnodes, markdown_to_blocks


class TestHTMLNode(unittest.TestCase):
    def my_patience_is_wavering(self):
        node = TextNode("",TextType.TEXT)
        nodes = text_to_textnodes(node)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes
        )
    

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_with_just_one_block(self):
        md = """
This is just one boring sentence
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            ["This is just one boring sentence"],
            blocks
        )

    def one_last_cool_test(self):
        md = """
This line has no fancy formating
But this _one_ does!

This is a **new** block
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This line has no fancy formating\nBut this _one_ does!",
                "This is a **new** block"
            ]
        )

if __name__ == "__main__":
    unittest.main()
