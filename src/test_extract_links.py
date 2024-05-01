import unittest
from extract_links import (
    extract_markdown_links,
    extract_markdown_images,
)


class ExtractLinksTest(unittest.TestCase):
    def test_extract_links_with_single_link(self):
        text = "text with a [link](https://www.example.com)"
        links = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("link", "https://www.example.com"),
            ],
            links
        )

    def test_extract_links_with_multiple_links(self):
        text = "text with a [link](https://www.example.com) text with another [link](https://www.example.com)"
        links = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("link", "https://www.example.com"),
                ("link", "https://www.example.com"),
            ],
            links
        )

    def test_extract_images_with_single_image(self):
        text = "text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)"
        links = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            ],
            links
        )

    def test_extract_images_with_multiple_images(self):
        text = "text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        links = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png"),
            ],
            links
        )


if __name__ == "__main__":
    unittest.main()
