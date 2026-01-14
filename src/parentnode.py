from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = {}):
        super().__init__(tag, None, children, props)

    def to_html(self):
        """Recursive function"""
        if self.tag == None:
            raise ValueError("Cannot convert parent node to HTML without a tag")
        if self.children == []:
            raise ValueError("Cannot convert parent node to HTML without children")
        result = ""
        for c in self.children:
            result += c.to_html()
        if self.props == {}:
            return f"<{self.tag}>{result}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"