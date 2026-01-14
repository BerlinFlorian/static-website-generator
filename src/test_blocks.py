import unittest
from blocks import BlockType, block_to_block_type

class TestBlocks(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        self.assertEqual(block_to_block_type("# heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("####### not heading"), BlockType.PARAGRAPH)

    def test_block_to_block_type_code(self):
        code = "```\nprint('hello')\n```"
        self.assertEqual(block_to_block_type(code), BlockType.CODE)

    def test_block_to_block_type_quote(self):
        quote = "> line 1\n> line 2"
        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)
        bad_quote = "> line 1\nline 2"
        self.assertEqual(block_to_block_type(bad_quote), BlockType.PARAGRAPH)

    def test_block_to_block_type_unordered(self):
        ul = "- item 1\n- item 2"
        self.assertEqual(block_to_block_type(ul), BlockType.UNORDERED_LIST)
        bad_ul = "- item 1\n* item 2"
        self.assertEqual(block_to_block_type(bad_ul), BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered(self):
        ol = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(ol), BlockType.ORDERED_LIST)
        bad_ol = "1. first\n3. third"
        self.assertEqual(block_to_block_type(bad_ol), BlockType.PARAGRAPH)

    def test_block_to_block_type_paragraph(self):
        self.assertEqual(block_to_block_type("Just a normal paragraph."), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()