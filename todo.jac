# todo.jac
node Task {
    has description: str;
    has done: bool = False;
}

with entry:__main__ {
    # create tasks directly on the root node
    root ++> Task("Do household cleaning");
    root ++> Task("Finish homework");
    root ++> Task("Prepare dinner");
    # --- list tasks ---
    tasks = [root --> Task];
    if not tasks {
        print("No tasks yet!");
    } else {
        i = 0;
        for t in tasks {
            i += 1;
        
            print(f"{i}. {t.description}");
        }
    }

    # complete a task by matching its description
    for t in tasks {
        if t.description == "Do household cleaning" {
            t.done = True;
            print(f"Completed task: {t.description}");
            break;
        }
    }

    #  list again to show the update
    tasks2 = [root --> Task];
    for t in tasks2 {
        status = ("✓" if t.done else "✗");
        print(f"[{status}] {t.description}");
    }
}
