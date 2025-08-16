import unittest

from blocktypes import block_to_block_type, BlockType


class TestBlockTypes(unittest.TestCase):
    def test_paragraph(self):
        block = """
This is simply a paragraph of text

It is built from two seperate blocks
"""
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH
        )
        block2 = "Just one sentence..."
        self.assertEqual(
            block_to_block_type(block2),
            BlockType.PARAGRAPH
        )

    def test_heading(self):
        block = "# This is a heading"
        block2 = "## This is a subheading"
        self.assertEqual(
            block_to_block_type(block),
            block_to_block_type(block2),
            BlockType.HEADING
        )

    def test_code(self):
        block = """```
print('Hello world!')
```"""
        block2 = "```\nfor i in range(10):\n  print(i)\n```"
        self.assertEqual(
            block_to_block_type(block),
            block_to_block_type(block2),
            BlockType.CODE
        )

    def test_quote(self):
        block = """
> Yesterday is History,
> Tomorrow is a Mystery,
> But Today is a Gift;
> That is why they call it The Present.
"""
        self.assertEqual(
            block_to_block_type(block),
            BlockType.QUOTE
        )

    def test_unordered_list(self):
        block = """
- eat
- sleep
- code
- repeat
"""
        self.assertEqual(
            block_to_block_type(block),
            BlockType.UNORDERED_LIST
        )

    def test_ordered_list(self):
        block = """
1. eat breakfast
2. eat lunch
3. each dinner
"""
        self.assertEqual(
            block_to_block_type(block),
            BlockType.ORDERED_LIST
        )

if __name__ == "__main__":
    unittest.main()
