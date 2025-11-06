

walker RepoMapper {
    static def clone_repo(repo_url) { 
        python:{
            from helpers.git_utils import clone_repo
            clone_repo(repo_url)
        end
    }

    static def get_local_path(repo_url) {
        path = python:
            from helpers.git_utils import local_path
            return local_path(repo_url)
        end
        return path
    }

    static def summarise_readme(repo_path) {
        summary = python:
            from helpers.file_tree import summarise_readme
            return summarise_readme(repo_path)
        end
        return summary
    }

    static def map_file_tree(repo_path) {
        tree = python:
            from helpers.file_tree import build_file_tree
            return build_file_tree(repo_path)
        end
        return tree
    }
 }
}