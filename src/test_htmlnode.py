import unittest
from htmlnode import HTMLNode, LeafNode


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
