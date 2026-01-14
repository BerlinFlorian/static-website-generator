import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zrf6x9C.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkj4.png)"
        matches = extract_markdown_images(text)
        expected = [
            ("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zrf6x9C.png"),
            ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkj4.png")
        ]
        self.assertEqual(matches, expected)

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.boot.dev)"
        matches = extract_markdown_links(text)
        expected = [
            ("link", "https://www.example.com"),
            ("another", "https://www.boot.dev")
        ]
        self.assertEqual(matches, expected)

    def test_extract_links_with_images(self):
        # On vérifie que extract_markdown_links ne capture PAS les images
        text = "Here is a ![image](url) and a [link](url_link)"
        matches = extract_markdown_links(text)
        # Actuellement, ton regex [ (.*?) ] capturing group capturerait aussi les images !
        # Si le test échoue, il faudra peut-être ajuster ton regex avec un lookbehind négatif.
        expected = [("link", "url_link")]
        self.assertEqual(matches, expected)

    def test_extract_markdown_images2(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


if __name__ == "__main__":
    unittest.main()