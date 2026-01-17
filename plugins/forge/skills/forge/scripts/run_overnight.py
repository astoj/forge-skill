#!/usr/bin/env python3
"""
Generate overnight automation script for Forge.
"""

import json
import sys
from pathlib import Path
from datetime import datetime


def generate_overnight_script(project_path: str = ".") -> str:
    """Generate overnight automation bash script."""

    project = Path(project_path).resolve()
    config_file = project / "forge.config.json"

    # Load config if exists
    if config_file.exists():
        with open(config_file) as f:
            config = json.load(f)
        project_name = config.get("project_name", project.name)
        current_phase = config.get("current_phase", 4)
    else:
        project_name = project.name
        current_phase = 4

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    script = f'''#!/bin/bash
# Forge Overnight Automation Script
# Generated: {datetime.now().isoformat()}
# Project: {project_name}

set -e

PROJECT_DIR="{project}"
LOG_FILE="$PROJECT_DIR/forge-overnight-{timestamp}.log"

echo "=== FORGE OVERNIGHT PIPELINE ===" | tee -a "$LOG_FILE"
echo "Started: $(date)" | tee -a "$LOG_FILE"
echo "Project: {project_name}" | tee -a "$LOG_FILE"

cd "$PROJECT_DIR"

# Create checkpoint
git tag "forge-overnight-{timestamp}" 2>/dev/null || true
echo "Checkpoint created: forge-overnight-{timestamp}" | tee -a "$LOG_FILE"

# Safety checks
echo "Running safety checks..." | tee -a "$LOG_FILE"

# Check git status
if [ -n "$(git status --porcelain)" ]; then
    echo "WARNING: Uncommitted changes detected" | tee -a "$LOG_FILE"
    git stash
    echo "Changes stashed" | tee -a "$LOG_FILE"
fi

# Run existing tests
if [ -f "package.json" ]; then
    npm test 2>&1 | tee -a "$LOG_FILE" || echo "Tests failed, continuing..." | tee -a "$LOG_FILE"
elif [ -f "requirements.txt" ] || [ -f "pyproject.toml" ]; then
    pytest 2>&1 | tee -a "$LOG_FILE" || echo "Tests failed, continuing..." | tee -a "$LOG_FILE"
fi

echo "Safety checks complete" | tee -a "$LOG_FILE"

# Main processing loop
echo "=== PROCESSING TASKS ===" | tee -a "$LOG_FILE"

ITERATION=0
MAX_ITERATIONS=100

while [ $ITERATION -lt $MAX_ITERATIONS ]; do
    ITERATION=$((ITERATION + 1))
    echo "--- Iteration $ITERATION ---" | tee -a "$LOG_FILE"

    # Get next task
    NEXT_TASK=$(task-master next --json 2>/dev/null | jq -r '.id // "NONE"')

    if [ "$NEXT_TASK" = "NONE" ] || [ -z "$NEXT_TASK" ]; then
        echo "No more tasks available" | tee -a "$LOG_FILE"
        break
    fi

    echo "Processing task: $NEXT_TASK" | tee -a "$LOG_FILE"

    # Process task with Claude
    claude -p "/ralph-loop \\"
Process Taskmaster task $NEXT_TASK:

1. Get details: task-master show $NEXT_TASK
2. /compound-engineering:plan based on task
3. /compound-engineering:work
4. /compound-engineering:review - fix any issues
5. task-master set-status --id $NEXT_TASK --status done

Output <promise>TASK_DONE</promise>
\\" --max-iterations 75 --completion-promise \\"TASK_DONE\\"" 2>&1 | tee -a "$LOG_FILE"

    echo "Task $NEXT_TASK processed" | tee -a "$LOG_FILE"
done

# Post-processing
echo "=== POST-PROCESSING ===" | tee -a "$LOG_FILE"

# Run tests
echo "Running final tests..." | tee -a "$LOG_FILE"
if [ -f "package.json" ]; then
    npm test 2>&1 | tee -a "$LOG_FILE" || true
elif [ -f "requirements.txt" ] || [ -f "pyproject.toml" ]; then
    pytest 2>&1 | tee -a "$LOG_FILE" || true
fi

# Generate summary
echo "=== SUMMARY ===" | tee -a "$LOG_FILE"
echo "Completed: $(date)" | tee -a "$LOG_FILE"
echo "Iterations: $ITERATION" | tee -a "$LOG_FILE"
echo "Remaining tasks: $(task-master list --status pending --count 2>/dev/null || echo 'unknown')" | tee -a "$LOG_FILE"

# Restore stashed changes if any
git stash pop 2>/dev/null || true

echo "=== OVERNIGHT COMPLETE ===" | tee -a "$LOG_FILE"
'''

    return script


if __name__ == "__main__":
    project_path = sys.argv[1] if len(sys.argv) > 1 else "."

    script = generate_overnight_script(project_path)

    # Output to file
    output_file = Path(project_path) / "forge-overnight.sh"
    with open(output_file, "w") as f:
        f.write(script)

    # Make executable
    output_file.chmod(0o755)

    print(f"Generated: {output_file}")
    print("Run with: ./forge-overnight.sh")
