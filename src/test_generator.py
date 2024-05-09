import unittest

from generator import extract_title

class TestHTMLNode(unittest.TestCase):

    def test_ExtractTitle(self):
        markdown =  "# ok"
        result = extract_title(markdown)
        self.assertEqual(result, "ok")
        
    def test_ExtractTitle(self):
        markdown = "#ok"
        with self.assertRaises(ValueError) as e:
            extract_title(markdown)
        self.assertEqual(str(e.exception), 'No title present, provide [ # your_title ]')
        
if __name__ == "__main__":
    unittest.main()
