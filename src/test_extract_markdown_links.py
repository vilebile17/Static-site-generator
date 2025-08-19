import unittest

from extract_markdown_links import extract_markdown_images, extract_markdown_links, extract_title
from textnode import TextNode, TextType


class TestMarkdownExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches) 
        
        matches2 = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches2)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", ("https://www.boot.dev"))], matches)


    def test_title_extractions(self):
        markdown = """
# This is a main heading

This is just some random old text 
"""
        self.assertEqual(
            extract_title(markdown),
            "This is a main heading"
        )

        markdown = "## Not a title"
        with self.assertRaises(ValueError) as cm:
            extract_title(markdown)
        self.assertEqual(str(cm.exception), "Selected markdown contains no <h1> title")


if __name__ == "__main__":
    unittest.main()
