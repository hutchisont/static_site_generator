import unittest

from inline_markdown import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


class InlineMarkdownTest(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
            ],
            nodes
        )

    def test_split_image(self):
       node = TextNode(
           "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
           text_type_text,
       )
       new_nodes = split_nodes_image([node])
       self.assertListEqual(
           [
               TextNode("This is text with an ", text_type_text),
               TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
           ],
           new_nodes,
       )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.com/image.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", text_type_image, "https://www.example.com/image.png"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second image", text_type_image, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
                TextNode(" and ", text_type_text),
                TextNode("another link", text_type_link, "https://blog.boot.dev"),
                TextNode(" with text that follows", text_type_text),
            ],
            new_nodes,
        )

    def test_no_delim(self):
        node = TextNode(
            "Some text with no formatting to delim on", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("Some text with no formatting to delim on",
                         text_type_text),
            ],
            new_nodes
        )

    def test_single_bold_delim(self):
        node = TextNode("Some **bold** text", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("Some ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" text", text_type_text),
            ],
            new_nodes
        )

    def test_two_bold_delim(self):
        node = TextNode("Some **bold** text plus **extra**", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("Some ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" text plus ", text_type_text),
                TextNode("extra", text_type_bold),
            ],
            new_nodes
        )

    def test_multiple_word_bold_delim(self):
        node = TextNode("Some **multi word bold** text", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("Some ", text_type_text),
                TextNode("multi word bold", text_type_bold),
                TextNode(" text", text_type_text),
            ],
            new_nodes
        )

    def test_single_italic_delim(self):
        node = TextNode("Some *italic* text", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("Some ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" text", text_type_text),
            ],
            new_nodes
        )

    def test_two_italic_delim(self):
        node = TextNode("Some *italic* text plus *extra*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("Some ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" text plus ", text_type_text),
                TextNode("extra", text_type_italic),
            ],
            new_nodes
        )

    def test_multiple_word_italic_delim(self):
        node = TextNode("Some *multi word italic* text", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("Some ", text_type_text),
                TextNode("multi word italic", text_type_italic),
                TextNode(" text", text_type_text),
            ],
            new_nodes
        )

    def test_single_code_delim(self):
        node = TextNode("Some `code` text", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("Some ", text_type_text),
                TextNode("code", text_type_code),
                TextNode(" text", text_type_text),
            ],
            new_nodes
        )

    def test_two_code_delim(self):
        node = TextNode("Some `code` text plus `extra`", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("Some ", text_type_text),
                TextNode("code", text_type_code),
                TextNode(" text plus ", text_type_text),
                TextNode("extra", text_type_code),
            ],
            new_nodes
        )

    def test_multiple_word_code_delim(self):
        node = TextNode("Some `multi word code` text", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("Some ", text_type_text),
                TextNode("multi word code", text_type_code),
                TextNode(" text", text_type_text),
            ],
            new_nodes
        )


if __name__ == "__main__":
    unittest.main()
