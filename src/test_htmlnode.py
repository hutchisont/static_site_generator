import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class HTMLNodeTest(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode("testtag",
                        "test value",
                        ["test"],
                        {
                            "testkey": "test val",
                            "testkey2": "test val2"
                        })
        actual = node.props_to_html()
        expected = " testkey=\"test val\" testkey2=\"test val2\""
        self.assertEqual(actual, expected)


class LeafNodeTest(unittest.TestCase):
    def test_leafnode_to_html_returns_expected_html(self):
        node = LeafNode("p", "test paragraph of text.")
        actual = node.to_html()
        expected = "<p>test paragraph of text.</p>"
        self.assertEqual(actual, expected)


class ParentNodeTest(unittest.TestCase):
    def test_parentnode_to_html_returns_expected_html_with_only_leaf_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        actual = node.to_html()
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(actual, expected)

    def test_parentnode_to_html_returns_expected_html_with_parent_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                ),
            ],
        )

        actual = node.to_html()
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>"
        self.assertEqual(actual, expected)
