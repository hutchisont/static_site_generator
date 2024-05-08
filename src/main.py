import shutil
import os

from block_markdown import markdown_to_html_node


def main():
    _static_to_public()
    _generate_page("content/index.md", "template.html", "public/index.html")


def _static_to_public():
    shutil.rmtree("public")
    shutil.copytree("static", "public")


def _extract_title(markdown: str):
    split_md = markdown.split("\n")
    title = ""
    for line in split_md:
        if line.startswith("# "):
            title = line.lstrip("# ")
            break

    if title == "":
        raise ValueError("All pages require an h1 header")

    return title


def _generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to\
            {dest_path} using {template_path}.")
    markdown = None
    with open(from_path) as f:
        markdown = f.read()

    template = None
    with open(template_path) as f:
        template = f.read()

    page_content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    generated_page_text = template.replace(
        "{{ Title }}", title).replace("{{ Content }}", page_content)

    just_path = os.path.dirname(dest_path)
    if not os.path.exists(just_path):
        os.makedirs(just_path)

    with open(dest_path, "w") as f:
        f.write(generated_page_text)


if __name__ == "__main__":
    main()
