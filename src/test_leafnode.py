import unittest
from leafnode import LeafNode


class LeafNodeTest(unittest.TestCase):
    def test_leafnode_to_html_returns_expected_html(self):
        node = LeafNode("p", "test paragraph of text.")
        actual = node.to_html()
        expected = "<p>test paragraph of text.</p>"
        self.assertEqual(actual, expected)
