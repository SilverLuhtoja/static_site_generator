import unittest

from htmlnode import LeafNode
from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


class TestTextNode(unittest.TestCase):
    # Test TextToTextNodes method
    class TextToTextNodes(unittest.TestCase):
        def test_SplitsCorrectly(self):
            text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
            new_nodes = text_to_textnodes(text)
            expected = [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image,
                         "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
            ]

            self.assertEqual(new_nodes, expected)
            
        def test_SmallerSplit(self):
                text = "This is **text** with an *italic* word"
                new_nodes = text_to_textnodes(text)
                expected = [
                    TextNode("This is ", text_type_text),
                    TextNode("text", text_type_bold),
                    TextNode(" with an ", text_type_text),
                    TextNode("italic", text_type_italic),
                    TextNode(" word", text_type_text),
                ]

                self.assertEqual(new_nodes, expected)
                
        def test_SmallerSplitWithLink(self):
                text = "This is [link](https://boot.dev) with an *italic* word and a **text**"
                new_nodes = text_to_textnodes(text)
                expected = [
                    TextNode("This is ", text_type_text),
                    TextNode("link", text_type_link, "https://boot.dev"),
                    TextNode(" with an ", text_type_text),
                    TextNode("italic", text_type_italic),
                    TextNode(" word and a ", text_type_text),
                    TextNode("text", text_type_bold),
                ]

                self.assertEqual(new_nodes, expected)


    # Test SplitNodesDelimeter method
    class SplitNodesDelimeter(unittest.TestCase):
        def test_SplitsCorrectly(self):
            node = TextNode(
                "This is text with a `code block` word", text_type_text)
            new_nodes = split_nodes_delimiter([node], "`", text_type_code)
            expected = [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ]

            self.assertEqual(new_nodes, expected)

        def test_Error(self):
            node = TextNode(
                "This is text with a `code block word", text_type_text)
            with self.assertRaises(ValueError):
                split_nodes_delimiter([node], "`", text_type_code)
                
     # Test SplitNodesDelimeter method
    class SplitNodesImage(unittest.TestCase):
        def test_SplitsCorrectly(self):
            node = TextNode(
                "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
                text_type_text,
            )


            new_nodes = split_nodes_image([node])
            expected = [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image,
                         "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
                ),
            ]
            self.assertEqual(new_nodes, expected)

    # Test SplitNodesLinks method
    class SplitNodesLinks(unittest.TestCase):
        def test_SplitsImagesCorrectly(self):
            node = TextNode(
                "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
                text_type_text,
            )
            new_nodes = split_nodes_link([node])
            self.assertListEqual(
                [
                    TextNode("This is text with a ", text_type_text),
                    TextNode("link", text_type_link, "https://boot.dev"),
                    TextNode(" and ", text_type_text),
                    TextNode("another link", text_type_link,
                            "https://blog.boot.dev"),
                    TextNode(" with text that follows", text_type_text),
                ],
                new_nodes,
            )

                
     # Test SplitNodesDelimeter method
    class ExtractMarkdown(unittest.TestCase):
        def test_ExtractsImages(self):
           text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
           excepted = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                       ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
           self.assertEqual(extract_markdown_images(text), excepted)
           
        def test_ExtractsLinks(self):
           text = text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
           excepted = [("link", "https://www.example.com"),("another", "https://www.example.com/another")]
           self.assertEqual(extract_markdown_links(text), excepted)

     


    def test_inner_test_class(self):
        suiteTextToTextNodes = unittest.defaultTestLoader.loadTestsFromTestCase(
            self.TextToTextNodes)
        suiteSplitNodesDelimeter = unittest.defaultTestLoader.loadTestsFromTestCase(
            self.SplitNodesDelimeter)
        suiteSplitNodesImage = unittest.defaultTestLoader.loadTestsFromTestCase(
            self.SplitNodesImage)
        suiteSplitNodesLinks = unittest.defaultTestLoader.loadTestsFromTestCase(
            self.SplitNodesLinks)
        suiteExtractMarkdown = unittest.defaultTestLoader.loadTestsFromTestCase(
            self.ExtractMarkdown)

        unittest.TextTestRunner().run(suiteTextToTextNodes)
        unittest.TextTestRunner().run(suiteSplitNodesDelimeter)
        unittest.TextTestRunner().run(suiteSplitNodesImage)
        unittest.TextTestRunner().run(suiteSplitNodesLinks)
        unittest.TextTestRunner().run(suiteExtractMarkdown)


if __name__ == "__main__":
    unittest.main()
