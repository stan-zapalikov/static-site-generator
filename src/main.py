from textnode import TextNode, TextType
from htmlnode import LeafNode

def main():
    testing = TextNode("aasdf", TextType.BOLD_TEXT, "czxv")
    print(testing)

    htmltesting = LeafNode("p", "Testing", {"href": "url", "ASD": 234})
    print(htmltesting.children)
    print(htmltesting)
    print(htmltesting.to_html())


main()
