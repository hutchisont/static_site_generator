import unittest

from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_paragraph,
    block_type_unordered_list,
    block_type_ordered_list,
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

    def test_block_to_block_type_heading(self):
        test_block_good = """# one
## two
### three
#### four
##### five
###### six"""

        block_type = block_to_block_type(test_block_good)
        self.assertEqual(block_type, block_type_heading)

        test_block_bad = """not a heading"""
        block_type = block_to_block_type(test_block_bad)
        self.assertNotEqual(block_type, block_type_heading)

        test_block_bad = """# this is but
this is not a heading
######## nor is this"""
        block_type = block_to_block_type(test_block_bad)
        self.assertNotEqual(block_type, block_type_heading)

    def test_block_to_block_type_code(self):
        test_block_good = """```
for fail in life:
    cringe
```"""
        block_type = block_to_block_type(test_block_good)
        self.assertEqual(block_type, block_type_code)

        test_block_bad = """not code block"""
        block_type = block_to_block_type(test_block_bad)
        self.assertNotEqual(block_type, block_type_code)

        test_block_bad = """```
not code block"""
        block_type = block_to_block_type(test_block_bad)
        self.assertNotEqual(block_type, block_type_code)

    def test_block_to_block_type_quote(self):
        test_block_good = """> all in life is
> rather difficult at times"""

        block_type = block_to_block_type(test_block_good)
        self.assertEqual(block_type, block_type_quote)

        test_block_bad = """not quote block"""
        block_type = block_to_block_type(test_block_bad)
        self.assertNotEqual(block_type, block_type_quote)

        test_block_bad = """> not quote block
but partially is"""
        block_type = block_to_block_type(test_block_bad)
        self.assertNotEqual(block_type, block_type_quote)

    def test_block_to_block_type_unordered_list(self):
        test_block_good = """* item
* another
- yet another"""

        block_type = block_to_block_type(test_block_good)
        self.assertEqual(block_type, block_type_unordered_list)

        test_block_bad = """not unordered list block"""
        block_type = block_to_block_type(test_block_bad)
        self.assertNotEqual(block_type, block_type_unordered_list)

        test_block_bad = """* partial list block
but partially is"""
        block_type = block_to_block_type(test_block_bad)
        self.assertNotEqual(block_type, block_type_unordered_list)

    def test_block_to_block_type_ordered_list(self):
        test_block_good = """1. item
2. second
3. third"""

        block_type = block_to_block_type(test_block_good)
        self.assertEqual(block_type, block_type_ordered_list)

        test_block_bad = """not ordered list block"""
        block_type = block_to_block_type(test_block_bad)
        self.assertNotEqual(block_type, block_type_ordered_list)

        test_block_bad = """1. partial ordered list block
3. but not numbered correctly"""
        block_type = block_to_block_type(test_block_bad)
        self.assertNotEqual(block_type, block_type_ordered_list)

    def test_block_to_block_type_paragraph(self):
        test_block_good = """just some random text, not like
there is good or bad to a paragraph block
its just some random text"""

        block_type = block_to_block_type(test_block_good)
        self.assertEqual(block_type, block_type_paragraph)


if __name__ == "__main__":
    unittest.main()
