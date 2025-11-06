# 🤖 Agentic Codebase Genius

A multi-agent Jac application that clones a GitHub repository, maps its file-tree,
analyses code, builds a Code Context Graph, and generates rich Markdown documentation.

## 🚀 Setup

```bash
python3 -m venv .env
source .env/bin/activate      # or .env\Scripts\activate
pip install -r requirements.txt
jac serve main.jac
