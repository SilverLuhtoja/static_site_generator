import unittest

from generator import extract_title

class TestHTMLNode(unittest.TestCase):

    def test_ExtractTitleOk(self):
        markdown =  "# ok title"
        result = extract_title(markdown)
        self.assertEqual(result, "ok title")
        
    def test_ExtractTitleFailWhenWrongFormat(self):
        markdown = "#ok"
        with self.assertRaises(ValueError) as e:
            extract_title(markdown)
        self.assertEqual(str(e.exception), 'No title present, provide [ # your_title ]')
        
    def test_ExtractTitleWhenNoH1(self):
        markdown = "## ok"
        with self.assertRaises(ValueError) as e:
            extract_title(markdown)
        self.assertEqual(str(e.exception),
                         'No title present, provide [ # your_title ]')
        
if __name__ == "__main__":
    unittest.main()
