import re

from block_type import (
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,
)

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)

    return filtered_blocks


def block_to_block_type(block_markdown):
    if _isHeading(block_markdown):
        return block_type_heading
    if _isCodeBlock(block_markdown):
        return block_type_code
    if _isQuoteBlock(block_markdown):
        return block_type_quote
    if _isUnorderedList(block_markdown):
        return block_type_unordered_list
    if _isOrderedList(block_markdown):
        return block_type_ordered_list
    return block_type_paragraph

def _isHeading(block):
    heading_markdown = block.split(" ")[0]
    if len(heading_markdown) > 6 or "#" not in heading_markdown:
        return False
    return True

def _isCodeBlock(block):
    regex = r"```([A-Za-z]*)?([\s\S]*?)```"
    return re.findall(regex, block)

def _isQuoteBlock(block):
    lines = block.split('\n')
    for line in lines:
        if not line.startswith(">"):
            return False
    return True

def _isUnorderedList(block):
    lines = block.split('\n')
    if block.startswith("* "):
        for line in lines:
            if line == "":
                continue
            if not line.startswith("* "):
                return False
        return True
    if block.startswith("- "):
        for line in lines:
            if line == "":
                continue
            if not line.startswith("- "):
                return False
        return True
    
def _isOrderedList(block):
    lines = block.split('\n')
    regex = r"\d.\s+"
    count=0
    for line in lines:
        if line == "":
            continue
        if not re.match(regex,line):
            return False
        
        line_nr = int(re.findall(r"\d",line)[0])
        if count+1 != line_nr :
            return False
        count = line_nr
        
    return True
