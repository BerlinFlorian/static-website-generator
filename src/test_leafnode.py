import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_basic(self):
        node = LeafNode("p", "This is a paragraph of text.", None)
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Just some raw text", None)
        self.assertEqual(node.to_html(), "Just some raw text")

    def test_to_html_with_value_none(self):
        node = LeafNode("p", None, None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_repr(self):
        node = LeafNode("b", "Bold text", {"class": "primary"})
        self.assertEqual(repr(node), "LeafNode(b, Bold text, {'class': 'primary'})")

if __name__ == "__main__":
    unittest.main()