import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestHTMLNode(unittest.TestCase):

    # Test PropsToHtml method
    class PropsToHtml(unittest.TestCase):
        def test_WhenPropsDefined(self):
            node = HTMLNode("", "", "", {"href": "https://www.google.com", "target": "_blank"})
            self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')
            
        def test_WhenPropsNotDefined(self):
            node = HTMLNode()
            self.assertEqual(node.props_to_html(), "")

    # Test Repr method
    class Repr(unittest.TestCase):
        def test_eq(self):
            child_node = HTMLNode("p", "child",)
            node = HTMLNode("p", "this is good", [child_node], {"target": "_blank"})
            expected = "HTMLNode(p, this is good, children: [HTMLNode(p, child, children: None, None)], {'target': '_blank'})"
            self.assertEqual(node.__str__(), expected)
  
    def test_inner_test_class(self):
        suitePropsToHtml = unittest.defaultTestLoader.loadTestsFromTestCase(self.PropsToHtml)
        suiteRepr = unittest.defaultTestLoader.loadTestsFromTestCase(self.Repr)

        unittest.TextTestRunner().run(suitePropsToHtml)
        unittest.TextTestRunner().run(suiteRepr)
        
        
class TestLeafNode(unittest.TestCase):

    # Test ToHtml method
    class ToHtml(unittest.TestCase):
        def test_to_html_no_children(self):
            node = LeafNode("p", "Hello, world!")
            self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
            
        def test_to_html_no_tag(self):
            node = LeafNode(None, "Hello, world!")
            self.assertEqual(node.to_html(), "Hello, world!")

    def test_inner_test_class(self):
        suiteToHtml = unittest.defaultTestLoader.loadTestsFromTestCase(
            self.ToHtml)

        unittest.TextTestRunner().run(suiteToHtml)


class TestParentNode(unittest.TestCase):
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
        
if __name__ == "__main__":
    unittest.main()
