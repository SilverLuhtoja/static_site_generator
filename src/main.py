from textnode import TextNode
from htmlnode import ParentNode, LeafNode

def main():
    # textnode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    textnode = TextNode("This is a text node", "bold")
    print(textnode)
    
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(node.to_html())

main()
