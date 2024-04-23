import unittest
from htmlnode import HTMLNode


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
