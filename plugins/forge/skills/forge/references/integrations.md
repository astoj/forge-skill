# Tool Integration Guide

## Taskmaster MCP

### Installation
```bash
npm install -g task-master-ai
```

### Configuration
Add to Claude Code MCP settings (`~/.claude/mcp_settings.json`):
```json
{
  "mcpServers": {
    "task-master-ai": {
      "command": "npx",
      "args": ["-y", "task-master-ai"]
    }
  }
}
```

### Key Commands

| Command | Purpose |
|---------|---------|
| `task-master init` | Initialize Taskmaster in project |
| `task-master parse-prd <file>` | Generate tasks from PRD |
| `task-master list` | List all tasks |
| `task-master next` | Get next task (deps satisfied) |
| `task-master show <id>` | Get task details |
| `task-master set-status --id <id> --status <status>` | Update status |
| `task-master analyze-complexity` | Analyze task complexity |
| `task-master expand --id <id>` | Break into subtasks |
| `task-master update <id> --notes "..."` | Add notes |

### Task Statuses
- `pending` - Not started
- `in-progress` - Currently being worked on
- `done` - Completed
- `blocked` - Cannot proceed

### Dependencies
Tasks with dependencies won't appear in `task-master next` until dependencies are complete.

---

## Compound Engineering Plugin

### Installation
```bash
/plugin marketplace add https://github.com/EveryInc/compound-engineering-plugin
/plugin install compound-engineering
```

### Commands

| Command | Purpose |
|---------|---------|
| `/compound-engineering:plan <description>` | Create implementation plan |
| `/compound-engineering:work <plan-file>` | Execute plan systematically |
| `/compound-engineering:review [PR#]` | Multi-agent code review |
| `/compound-engineering:triage` | Triage review findings |
| `/compound-engineering:resolve_todo_parallel` | Resolve todos in parallel |

### The Compound Loop

```
PLAN -> WORK -> REVIEW -> CODIFY -> (repeat)
```

Each cycle compounds knowledge:
- Plans inform future plans
- Reviews catch more issues
- Patterns get documented

### Best Practices
- Always start with `/compound-engineering:plan`
- Run `/compound-engineering:review` before merging
- Use `/compound-engineering:triage` to process findings
- Document learnings for future reference

---

## Ralph Wiggum Plugin

### Installation
```bash
/plugin install ralph-wiggum@claude-plugins-official
```

### Command Syntax
```bash
/ralph-loop "<prompt>" --max-iterations N --completion-promise "TEXT"
```

### Parameters
- `--max-iterations`: Safety limit (ALWAYS SET THIS)
- `--completion-promise`: Exact text that signals completion

### How It Works
1. You run the command once
2. Claude works on the task
3. When Claude tries to exit, the Stop hook intercepts
4. The same prompt is fed back with updated context
5. Loop continues until completion promise found or max iterations reached

### Safety Rules
- ALWAYS set `--max-iterations`
- Use specific completion promises
- Include fallback instructions for being stuck
- Create git checkpoints before long runs

### Effective Prompts
```bash
/ralph-loop "
[Clear task description]

Requirements:
- Requirement 1
- Requirement 2

Success criteria:
- Criterion 1
- Criterion 2

If stuck after 10 iterations:
- Document blockers
- Move to next task

Output <promise>TASK_COMPLETE</promise> when all criteria met.
" --max-iterations 30 --completion-promise "TASK_COMPLETE"
```

---

## Combining All Three

### Task Processing Pattern
```bash
# Get next task from Taskmaster
TASK=$(task-master next)

# Process with Compound Engineering inside Ralph loop
/ralph-loop "
Process Taskmaster task $TASK:

1. /compound-engineering:plan based on task details
2. /compound-engineering:work on the plan
3. /compound-engineering:review the changes
4. Fix any issues found
5. Mark complete: task-master set-status --id $TASK --status done

Output <promise>TASK_DONE</promise>
" --max-iterations 50 --completion-promise "TASK_DONE"
```

### Overnight Automation
```bash
#!/bin/bash
# overnight.sh

while true; do
  TASK=$(task-master next --json | jq -r '.id // "NONE"')

  if [ "$TASK" = "NONE" ]; then
    echo "All tasks complete!"
    break
  fi

  claude -p "/ralph-loop 'Process task $TASK with compound engineering. Output <promise>DONE</promise>' --max-iterations 75 --completion-promise 'DONE'"
done
```
