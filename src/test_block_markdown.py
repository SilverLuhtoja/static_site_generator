import unittest

from block_markdown import block_to_block_type, markdown_to_blocks
from block_type import (
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,
)


class TestMarkdownToHTML(unittest.TestCase):
    # Test TextToTextNodes method
    class MarkdownToBlocks(unittest.TestCase):
        def test_Size(self):
            text = """
            This is **bolded ** paragraph

            This is another paragraph with *italic * text and `code` here
            This is the same paragraph on a new line

            * This is a list
            * with items    
            """
        
            result_list = markdown_to_blocks(text)
            self.assertEqual(len(result_list), 3)
            
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )


    class BlockToBlockTypes(unittest.TestCase):
        def test_Heading(self):
            block_text = "# Heading"
            result = block_to_block_type(block_text)
            
            self.assertEqual(result, block_type_heading)
            
        def test_CodeBlock(self):
            block_text = "```This is code block```"
            result = block_to_block_type(block_text)
            
            self.assertEqual(result, block_type_code)
            
        def test_QuoteBlock(self):
            block_text = ">this\n>is\n>quote block"
            result = block_to_block_type(block_text)
            
            self.assertEqual(result, block_type_quote)
            
        def test_NotQuoteBlock(self):
            block_text = ">this\n>is\nquote block"
            result = block_to_block_type(block_text)
            
            self.assertNotEqual(result, block_type_quote)

        def test_UnorderedList(self):
            block_text = "* 1\n* 2\n* 3\n"
            result = block_to_block_type(block_text)
            
            self.assertEqual(result, block_type_unordered_list)
            
        def test_UnorderedListMixedStarts(self):
            block_text = "* 1\n- 2\n* 3\n"
            result = block_to_block_type(block_text)
            
            self.assertNotEqual(result, block_type_unordered_list)
            
        def test_NotUnorderedList(self):
            block_text = "* 1\n*2\n* 3\n"
            result = block_to_block_type(block_text)
            
            self.assertNotEqual(result, block_type_unordered_list)
            
        def test_OrderedList(self):
            block_text = "1. one\n2. two\n3. three"
            result = block_to_block_type(block_text)
            
            self.assertEqual(result, block_type_ordered_list)

        def test_NotOrderedList(self):
            block_text = "1. one\n3. three\n4. four\n"
            result = block_to_block_type(block_text)
            
            self.assertNotEqual(result, block_type_ordered_list)
            
        def test_Paragraph(self):
            block_text = "Im regular paragraph"
            result = block_to_block_type(block_text)
            
            self.assertEqual(result, block_type_paragraph)
        
        
    def test_inner_test_class(self):
        suiteMarkdownToBlocks = unittest.defaultTestLoader.loadTestsFromTestCase(
            self.MarkdownToBlocks)
        suiteBlockToBlockTypes = unittest.defaultTestLoader.loadTestsFromTestCase(
            self.BlockToBlockTypes)
      
        unittest.TextTestRunner().run(suiteMarkdownToBlocks)
        unittest.TextTestRunner().run(suiteBlockToBlockTypes)


if __name__ == "__main__":
    unittest.main()
