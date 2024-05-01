def markdown_to_blocks(document_text: str) -> list:
    split_text = document_text.split("\n\n")
    blocks = []
    for line in split_text:
        if line == "":
            continue
        blocks.append(line.strip())
    return blocks
