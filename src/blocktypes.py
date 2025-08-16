from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(block):
    if block[0] == "#":
        return BlockType.HEADING
    elif block[:3] == "```" and block[-3:] == "```":
        return BlockType.CODE

    lines = block.split("\n")
    quote = True
    unordered_list = True
    ordered_list = True
    iteration_count = 1
    for line in lines:
        if line:
            quote = quote and line[0] == ">"
            unordered_list = unordered_list and (line[:2] == "- ")
            ordered_list = ordered_list and (line[:3] == f"{iteration_count}. ")
            iteration_count += 1

    if quote:
        return BlockType.QUOTE
    elif unordered_list:
        return BlockType.UNORDERED_LIST
    elif ordered_list:
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
