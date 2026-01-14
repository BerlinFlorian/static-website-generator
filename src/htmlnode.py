
class HTMLNode:
    def __init__(self, tag = None, value = None, children = [], props = {}):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None or self.props == {}:
            return ""
        html = " "
        for key, value in self.props.items():
            html += f"{key}=\"{value}\" "
        return html

    def __repr__(self):
        if self.tag == None:
            return f"<HTMLNode value=\"{self.value}\">"
        elif self.value == None:
            result = ""
            for c in children:
                result += c.to_html()
            if self.props == {}:
                return f"<{self.tag}>{result}</{self.tag}>"
            return f"<{self.tag}{self.props_to_html()}>\n{result}\n</{self.tag}>"
        elif self.children == []:
            if self.props == {}:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return ""