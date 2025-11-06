import os
import git
from git import Repo

def clone_repo(url, base="clones"):
    os.makedirs(base, exist_ok=True)
    name = url.split("/")[-1].replace(".git","")
    path = os.path.join(base, name)
    if not os.path.exists(path):
        print(f"Cloning {url}...")
        git.Repo.clone_from(url, path)
    else:
        print("Repo already cloned.")
    return path

def local_path(url, base="clones"):
    name = url.split("/")[-1].replace(".git","")
    return os.path.join(base, name)
