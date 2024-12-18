from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    testing = TextNode("aasdf", TextType.BOLD_TEXT, "czxv")
    print(testing)

    htmltesting = HTMLNode("<p>", "Testing", [1, 2, 3], {"href": "url"})
    print(htmltesting)


main()
