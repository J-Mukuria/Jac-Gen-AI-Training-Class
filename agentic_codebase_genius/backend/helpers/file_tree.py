import os

IGNORE_DIRS = {'.git', 'node_modules', '__pycache__'}

def build_file_tree(base):
    tree = {}
    for root, dirs, files in os.walk(base):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        rel = os.path.relpath(root, base)
        tree[rel] = files
    return tree

def summarise_readme(base):
    readme = os.path.join(base, "README.md")
    if not os.path.exists(readme):
        return "No README found."
    text = open(readme, encoding="utf-8").read()
    return text[:600] + ("..." if len(text)>600 else "")
