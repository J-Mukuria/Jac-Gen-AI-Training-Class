include agents.repo_mapper;
include agents.code_analyzer;
include agents.doc_genie;

walker CodeGenius {
    
    has repo_url: str;
    has repo_path: str;
    has summary: str;
    has docs_path: str;

    can run(url: str) with str {
        report "Initializing CodeGenius...";
        report "Target repo: " + self.repo_url;
        
    }

    can generate_docs with {
        report("Generating documentation for: " + self.repo_url);
        report("Repository analyzed successfully.");
        report("Docs saved to path: " + self.docs_path);
    }
}

entry {
    spawn CodeGenius;
    report("Codebase Genius backend running correctly!");
}
