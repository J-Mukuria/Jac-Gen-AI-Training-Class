walker DocGenie {
    static def create_docs(repo_path: summary, ccg:){
        output = python;
     from helpers.parser_utils import render_markdown
         return render_markdown(repo_path, summary, ccg)
        end
        return output
    }
}
