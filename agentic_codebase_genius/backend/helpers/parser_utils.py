import os
import re 
from helpers.visualizer import make_diagram

def build_ccg(path):
    graph = {}
    for root, _, files in os.walk(path):
        for f in files:
            if f.endswith((".py",".jac")):
                fp = os.path.join(root, f)
                content = open(fp, encoding="utf-8").read()
                funcs = re.findall(r'def\\s+(\\w+)', content)
                graph[f] = {"functions": funcs, "calls": []}
    make_diagram(graph, path)
    return graph

def describe_function(repo_path, func):
    result = []
    for root, _, files in os.walk(repo_path):
        for f in files:
            if f.endswith(".py"):
                with open(os.path.join(root,f)) as fh:
                    if func in fh.read():
                        result.append(f)
    return {"function": func, "found_in": result}

def render_markdown(path, summary, ccg):
    repo = os.path.basename(path)
    outdir = os.path.join("outputs", repo)
    os.makedirs(outdir, exist_ok=True)
    doc_path = os.path.join(outdir, "docs.md")
    with open(doc_path,"w",encoding="utf-8") as f:
        f.write(f"# 📘 {repo} Documentation\\n\\n")
        f.write("## Overview\\n"+summary+"\\n\\n")
        f.write("## Code Context Graph\\n")
        for file,info in ccg.items():
            f.write(f"- **{file}**: {len(info['functions'])} functions → {info['functions']}\\n")
        f.write("\\n![Diagram](diagram.png)\\n")
    return doc_path
