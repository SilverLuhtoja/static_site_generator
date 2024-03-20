class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, otherTextNode):
        return self.text == otherTextNode.text and self.text_type == otherTextNode.text_type and self.url == otherTextNode.url

    def __repr__(self) -> str:
        return 'TextNode({0}, {1}, {2})'.format(self.text, self.text_type, self.url)
