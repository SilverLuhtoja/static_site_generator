import unittest

from html_setup import heading_block_to_html, paragraph_block_to_html, quote_block_to_html, un_list_to_html, ord_list_to_html, code_block_to_html
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode


class TestHTMLNode(unittest.TestCase):

    def test_QuoteBlockToHtml(self):
        markdown = "> this is a quote"
        result = quote_block_to_html(markdown)
        expected = "<blockquote>this is a quote</blockquote>"
        self.assertEqual(result, expected)

    def test_UnListToHtml(self):
        markdown = "* item1\n* item2"
        result = un_list_to_html(markdown)
        expected = "<ul><li>item1</li><li>item2</li></ul>"
        self.assertEqual(result, expected)

    def test_OrdListToHtml(self):
        markdown = "1. item1\n2. item2"
        result = ord_list_to_html(markdown)
        expected = "<ol><li>item1</li><li>item2</li></ol>"
        self.assertEqual(result, expected)
        
    def test_CodeBlockToHtml(self):
        markdown = "```thisIsCodeBlock```"
        result = code_block_to_html(markdown)
        expected = "<code><pre>thisIsCodeBlock</pre></code>"
        self.assertEqual(result, expected)

    def test_HeadingBlockToHtml(self):
        markdown = "### is h3"
        result = heading_block_to_html(markdown)
        expected = "<h3>is h3</h3>"
        self.assertEqual(result, expected)
        
        
    def test_ParagraphBlockToHtml(self):
        markdown = "sentence"
        result = paragraph_block_to_html(markdown)
        expected = "<p>sentence</p>"
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
