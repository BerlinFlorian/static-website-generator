import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "Click me!",
            None,
            {"href": "https://www.google.com", "target": "_blank"}
        )
        # Expecting the leading space and trailing space based on current implementation
        expected = ' href="https://www.google.com" target="_blank" '
        self.assertEqual(node.props_to_html(), expected)

    def test_values(self):
        node = HTMLNode("p", "Hello world")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello world")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_repr(self):
        node = HTMLNode("p", "Hello world")
        self.assertEqual(repr(node), "<p>Hello world</p>")

    def test_to_html_error(self):
        node = HTMLNode("p", "Hello world")
        with self.assertRaises(NotImplementedError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()