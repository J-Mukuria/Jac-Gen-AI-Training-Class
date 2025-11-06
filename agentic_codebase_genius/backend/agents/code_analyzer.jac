walker CodeAnalyzer {
    static def build_ccg(repo_path) {
        ccg = python:
            from helpers.parser_utils import build_ccg
            return build_ccg(repo_path)
        end
        return ccg
    }

    static def describe_function(repo_path, func_name) {
        desc = python:
            from helpers.parser_utils import describe_function
            return describe_function(repo_path, func_name)
        end
        return desc
    }
}
