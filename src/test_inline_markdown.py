import unittest
from inline_markdown import (
    split_nodes_delimiter,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


class InlineMarkdownTest(unittest.TestCase):
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
