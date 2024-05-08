import shutil
import os

from block_markdown import markdown_to_html_node


def main():
    _static_to_public()
    # _generate_page("content/index.md", "template.html", "public/index.html")
    _generate_all_pages("content", "template.html", "public")


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
    print(f"Generating page from {from_path} to {
          dest_path} using {template_path}.")
    markdown = None
    with open(from_path) as f:
        markdown = f.read()

    template = None
    with open(template_path) as f:
        template = f.read()

    page_content = markdown_to_html_node(markdown).to_html()
    title = _extract_title(markdown)

    generated_page_text = template.replace(
        "{{ Title }}", title).replace("{{ Content }}", page_content)

    just_path = os.path.dirname(dest_path)
    print(f"just path: {just_path}")
    if just_path and not os.path.exists(just_path):
        os.makedirs(just_path)

    new_filename = os.path.basename(from_path).split(".")[0] + ".html"

    with open(dest_path + new_filename, "w") as f:
        f.write(generated_page_text)


def _generate_all_pages(content_dir_path: str, template_path: str, dest_dir_path: str):
    for root, subdirs, files in os.walk(content_dir_path):
        print(f"root: {root}\nsubdirs: {subdirs}\nfiles: {files}")
        for file in files:
            from_file = os.path.join(root, file)
            print(from_file)
            _generate_page(from_file, template_path,
                           dest_dir_path + "/" + root.replace("content/", "").replace("content", "") + "/")


if __name__ == "__main__":
    main()
