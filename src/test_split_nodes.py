import unittest

from textnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link


class TestSplitImages(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )

    def test_just_an_image(self):
        node = TextNode(
        "![donkey kong](donkey-kong.png)",
        TextType.TEXT,
    )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
        [
            TextNode("donkey kong", TextType.IMAGE, "donkey-kong.png"),
        ],
        new_nodes,
    )



class TestSplitLinks(unittest.TestCase):
    def split_one_link(self):
        node = TextNode(
            "This has a link to [github](www.github.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This has a link to ", TextType.TEXT),
                TextNode("github", TextType.LINK, "www.github.com")
            ],
            new_nodes
        )

    def rickroll(self):
        node = TextNode("Never gonna give you up,", TextType.TEXT)
        node2 = TextNode("Never gonna let you down,", TextType.TEXT)
        node3 = TextNode("Never gonna turn around", TextType.TEXT)
        node4 = TextNode("and desert you.", TextType.TEXT)
        node5 = TextNode("- [Rick](https://www.youtube.com/channel/UCuAXFkgsw1L7xaCfnd5JJOw) Astley")
        new_nodes = split_nodes_link([node,node2,node3,node4,node5])
        self.assertListEqual(
            [
                TextNode("Never gonna give you up,", TextType.TEXT),
                TextNode("Never gonna let you down,", TextType.TEXT),
                TextNode("Never gonna turn around", TextType.TEXT),
                TextNode("and desert you.", TextType.TEXT),
                TextNode("- ", TextType.TEXT),
                TextNode("Rick", TextType.LINK, "https://www.youtube.com/channel/UCuAXFkgsw1L7xaCfnd5JJOw"),
                TextNode(" Astley", TextType.TEXT)

            ]
        )
        
    





if __name__ == "__main__":
    unittest.main()
