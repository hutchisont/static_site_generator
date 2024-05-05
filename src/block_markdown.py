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
