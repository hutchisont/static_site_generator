import unittest

from block_markdown import (
    markdown_to_blocks,
)


class BlockMarkdownTest(unittest.TestCase):
    def test_markdown_to_blocks(self):
        test_text = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""

        blocks = markdown_to_blocks(test_text)

        self.assertListEqual(
            [
                "This is **bolded** paragraph",
                """This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line""",
                """* This is a list
* with items""",
            ],
            blocks,
        )


if __name__ == "__main__":
    unittest.main()
