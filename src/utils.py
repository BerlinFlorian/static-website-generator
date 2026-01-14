import os
import shutil
from extract_markdown import markdown_to_html_node
from split import extract_title

def source_to_target(source, target):
    """RECURCIVE function that copy all contents from a source directory to a target directory:
        -it should first delete all contents of the destination directory to ensure that the copy is clean
        - copy all files and subdirectories, nested files, etc
        - it should handle errors gracefully and provide informative messages
        - log the path of each file and directory copied"""
    if not os.path.exists(target):
        os.makedirs(target)
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        target_path = os.path.join(target, item)
        if os.path.isdir(source_path):
            source_to_target(source_path, target_path)
        else:
            shutil.copy2(source_path, target_path)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    node = markdown_to_html_node(markdown_content)
    html_content = node.to_html()

    title = extract_title(markdown_content)

    full_html = template_content.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html_content)

    full_html = full_html.replace('href="/', f'href="{basepath}')
    full_html = full_html.replace('src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(full_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    entries = os.listdir(dir_path_content)

    for entry in entries:
        from_path = os.path.join(dir_path_content, entry)

        if os.path.isfile(from_path):
            if entry.endswith(".md"):
                dest_name = entry.replace(".md", ".html")
                dest_path = os.path.join(dest_dir_path, dest_name)
                generate_page(from_path, template_path, dest_path, basepath)
        else:
            new_dest_dir = os.path.join(dest_dir_path, entry)
            generate_pages_recursive(from_path, template_path, new_dest_dir, basepath)
