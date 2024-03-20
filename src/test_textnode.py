import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):

    # Test Eq method
    class Eq(unittest.TestCase):
        def test_eq(self):
            node = TextNode("This is a text node", "bold")
            node2 = TextNode("This is a text node", "bold")
            self.assertEqual(node, node2)

        def test_whenUrlsNone_ReturnTrue(self):
            node = TextNode("This is a text node", "bold", None)
            node2 = TextNode("This is a text node", "bold", None)
            self.assertEqual(node, node2)

        def test_whenDifferentFieldValues_ReturnFalse(self):
            node = TextNode("This is a text image", "bold")
            node2 = TextNode("This is a text node", "bold")
            self.assertNotEqual(node, node2)

    # Test Repr method
    class Repr(unittest.TestCase):
        def test_ReturnsExpectedRepresitation(self):
            node = TextNode("This is a text node", "bold", "www.google.com")
            stringOfNode = node.__str__()
            self.assertEqual(stringOfNode, "TextNode(This is a text node, bold, www.google.com)")
            
        def test_ReturnsExpectedRepresitationWhenUrlNone(self):
            node = TextNode("This is a text node", "bold")
            stringOfNode = node.__str__()
            self.assertEqual(stringOfNode, "TextNode(This is a text node, bold, None)")




    def test_inner_test_class(self):
        suiteEq = unittest.defaultTestLoader.loadTestsFromTestCase(self.Eq)
        suiteRepr = unittest.defaultTestLoader.loadTestsFromTestCase(self.Repr)
        unittest.TextTestRunner().run(suiteEq)
        unittest.TextTestRunner().run(suiteRepr)


if __name__ == "__main__":
    unittest.main()
