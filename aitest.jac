# todo_ai_interactive_fixed.jac
import from byllm.llm {Model}

glob llm = Model(model_name="gemini/gemini-2.0-flash", verbose=False);

def suggest_deadline(task: str) -> str by llm();

# todo.jac
node Task {
    has description: str;
    has done: bool = False;
    has deadline: str = "not set";
}

with entry:__main__ {
    # create tasks directly on the root node
    root ++> Task("Do household cleaning");
    root ++> Task("Finish homework");
    root ++> Task("Prepare dinner");
    new_task.deadline = suggest_deadline(new_task.description);
    print(f"Task added: {new_task.description} (Deadline suggestion: {new_task.deadline})");
    # --- list tasks ---
    tasks = [root --> Task];
    if not tasks {
        print("No tasks yet!");
    } else {
        i = 0;
        for t in tasks {
            i += 1;
        
            print(f"[ {t.description} (Deadline: {t.deadline})");
        }
    }

    # complete a task by matching its description
    for t in tasks {
        if t.description == "Do household cleaning" {
            t.done = True;
            print(f"Completed task: {here.description}");
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
