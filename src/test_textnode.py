import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a different text node", TextType.ITALIC)
        node4 = TextNode("This is a text node", TextType.CODE)
        node5 = TextNode("This is a link", TextType.LINK, "google.com")
        node6 = TextNode("This is an image", TextType.IMAGE, "bigchungus.png")
        self.assertEqual(node, node2)
        self.assertNotEqual(node,node3)
        self.assertNotEqual(node5,node3)
        self.assertNotEqual(node4,node3)
        self.assertNotEqual(node2,node6)
        self.assertNotEqual(node5,node)

        


if __name__ == "__main__":
    unittest.main()
