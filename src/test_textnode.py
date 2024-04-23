import unittest
from textnode import TextNode


class TextTextNode(unittest.TestCase):
    def test_when_contents_same_eq_returns_true(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

        node = TextNode("This is a text node with url",
                        "bold",
                        "http://testurl")
        node2 = TextNode("This is a text node with url",
                         "bold",
                         "http://testurl")
        self.assertEqual(node, node2)

    def test_when_contents_not_same_eq_returns_false(self):
        node = TextNode("This is a text node with url",
                        "bold",
                        "http://testurl")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_repr_returns_correct_string(self):
        node = TextNode("This is a text node", "bold")
        expected = "TextNode(This is a text node, bold, None)"
        self.assertEqual(node.__repr__(), expected)

        node = TextNode("This is a text node", "bold", "http://testurl")
        expected = "TextNode(This is a text node, bold, http://testurl)"
        self.assertEqual(node.__repr__(), expected)


if __name__ == "__main__":
    unittest.main()
