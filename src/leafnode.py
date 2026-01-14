from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = {}):
        if props == None:
            props = {}
        super().__init__(tag, value, [], props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Cannot convert leaf node to HTML without a value")
        if self.tag == None:
            return self.value
        if self.props == {}:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


