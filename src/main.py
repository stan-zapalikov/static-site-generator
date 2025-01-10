import os
import shutil
from leafnode import LeafNode
from block import markdown_to_html_node

def main():
    if (os.path.exists('public')):
        shutil.rmtree('public')
    os.mkdir('public')

    copy_static('static', 'public')
    generate_pages_recursive("content/", "template.html", "public/")

def copy_static(source, destination):
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
        if os.path.isdir(source_path):
            os.mkdir(dest_path)
            copy_static(source_path, dest_path)

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    text_from_file = ""
    html_template = ""
    with open(from_path, "r") as mdFile:
        text_from_file = mdFile.read()
    with open(template_path, "r") as template:
        html_template = template.read()
    converted_text = markdown_to_html_node(text_from_file).to_html()
    title = extract_title(text_from_file)
    html_template = html_template.replace("{{ Title }}", title)
    html_template = html_template.replace("{{ Content }}", converted_text)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as to_file:
        to_file.write(html_template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        source_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(source_path):
            generate_page(source_path, template_path, dest_path[:-2] + "html")
        if os.path.isdir(source_path):
            os.mkdir(dest_path)
            generate_pages_recursive(source_path, template_path, dest_path)




main()
