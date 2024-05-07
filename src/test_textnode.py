import unittest

from htmlnode import LeafNode
from textnode import (
    TextNode,
    text_node_to_html_node,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)



class TestTextNode(unittest.TestCase):

    # Test Eq method
    class Eq(unittest.TestCase):
        def test_eq(self):
            node = TextNode("This is a text node", text_type_bold)
            node2 = TextNode("This is a text node", text_type_bold)
            self.assertEqual(node, node2)

        def test_whenUrlsNone_ReturnTrue(self):
            node = TextNode("This is a text node", text_type_bold, None)
            node2 = TextNode("This is a text node", text_type_bold, None)
            self.assertEqual(node, node2)

        def test_whenDifferentFieldValues_ReturnFalse(self):
            node = TextNode("This is a text image", text_type_bold)
            node2 = TextNode("This is a text node", text_type_bold)
            self.assertNotEqual(node, node2)

    # Test Repr method
    class Repr(unittest.TestCase):
        def test_ReturnsExpectedRepresitation(self):
            node = TextNode("This is a text node", text_type_bold, "www.google.com")
            stringOfNode = node.__str__()
            self.assertEqual(stringOfNode, "TextNode(This is a text node, bold, www.google.com)")
            
        def test_ReturnsExpectedRepresitationWhenUrlNone(self):
            node = TextNode("This is a text node", text_type_bold)
            stringOfNode = node.__str__()
            self.assertEqual(stringOfNode, "TextNode(This is a text node, bold, None)")
            
    # Test TextNodeToHtmlNode method
    class TextNodeToHtmlNode(unittest.TestCase):
        def test_Text(self):
            node = TextNode("tere tere", text_type_text)
            self.assertEqual(text_node_to_html_node(
                node).to_html(), LeafNode(None, "tere tere").to_html())
            
    def test_inner_test_class(self):
        suiteEq = unittest.defaultTestLoader.loadTestsFromTestCase(self.Eq)
        suiteRepr = unittest.defaultTestLoader.loadTestsFromTestCase(self.Repr)
        suiteTextNodeToHtmlNode = unittest.defaultTestLoader.loadTestsFromTestCase(
            self.TextNodeToHtmlNode)
        
        unittest.TextTestRunner().run(suiteEq)
        unittest.TextTestRunner().run(suiteRepr)
        unittest.TextTestRunner().run(suiteTextNodeToHtmlNode)


if __name__ == "__main__":
    unittest.main()
