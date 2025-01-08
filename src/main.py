import os
import shutil
from src.leafnode import LeafNode

def main():
    if (os.path.exists('public')):
        shutil.rmtree('public')
    os.mkdir('public')

    copy_static('static', 'public')

def copy_static(source, destination):
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
        if os.path.isdir(source_path):
            os.mkdir(dest_path)
            copy_static(source_path, dest_path)

def extract_title(markdown):
    firstLine = markdown.split("\n")[0]
    if (firstLine[0] != "#"):
        raise Exception("No title found")
    return LeafNode("h1", firstLine[2:])


main()
