from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node


block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(document_text: str) -> list:
    split_text = document_text.split("\n\n")
    blocks = []
    for line in split_text:
        if line == "":
            continue
        blocks.append(line.strip())
    return blocks


def block_to_block_type(input_block: str) -> str:
    split_block = input_block.split('\n')
    if _check_for_heading(split_block) is True:
        return block_type_heading
    if _check_for_code(split_block) is True:
        return block_type_code
    if _check_for_quote(split_block) is True:
        return block_type_quote
    if _check_for_unordered_list(split_block) is True:
        return block_type_unordered_list
    if _check_for_ordered_list(split_block) is True:
        return block_type_ordered_list
    return block_type_paragraph


def _check_for_heading(lines_to_check: list) -> bool:
    headings = ("#", "##", "###", "####", "#####", "######")
    for line in lines_to_check:
        if not line.startswith(headings):
            return False

    return True


def _check_for_code(lines_to_check: list) -> bool:
    code_block_tag = "```"
    if len(lines_to_check) > 2:
        return (lines_to_check[0] == code_block_tag and
                lines_to_check[-1] == code_block_tag)

    return False


def _check_for_quote(lines_to_check: list) -> bool:
    for line in lines_to_check:
        if not line.startswith(">"):
            return False
    return True


def _check_for_unordered_list(lines_to_check: list) -> bool:
    tags = ("* ", "- ")
    for line in lines_to_check:
        if not line.startswith(tags):
            return False

    return True


def _check_for_ordered_list(lines_to_check: list) -> bool:
    for i in range(0, len(lines_to_check)):
        tag = f"{i+1}. "
        if not lines_to_check[i].startswith(tag):
            return False

    return True


def markdown_to_html_node(markdown_document: str) -> list:
    blocks = markdown_to_blocks(markdown_document)
    html_nodes = []
    for block in blocks:
        node = block_to_html_node(block)
        html_nodes.append(node)

    return ParentNode("div", html_nodes, None)


def block_to_html_node(block: str):
    block_type = block_to_block_type(block)
    if block_type == block_type_heading:
        return _heading_block_to_html_node(block)
    if block_type == block_type_code:
        return _code_block_to_html_node(block)
    if block_type == block_type_quote:
        return _quote_block_to_html_node(block)
    if block_type == block_type_ordered_list:
        return _ordered_list_block_to_html_node(block)
    if block_type == block_type_unordered_list:
        return _unordered_list_block_to_html_node(block)
    if block_type == block_type_paragraph:
        return _paragraph_block_to_html_node(block)
    raise ValueError("Invalid block type")


def text_to_children(text: str):
    nodes = text_to_textnodes(text)
    children = []

    for node in nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)

    return children


def _heading_block_to_html_node(block: str):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break

    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")

    text = block[level + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def _code_block_to_html_node(block: str):
    if not _check_for_code(block.split("\n")):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def _quote_block_to_html_node(block: str):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def _ordered_list_block_to_html_node(block: str):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def _unordered_list_block_to_html_node(block: str):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def _paragraph_block_to_html_node(block: str):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)
