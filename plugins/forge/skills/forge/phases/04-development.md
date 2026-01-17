# Phase 4: Development

## Objective
Implement all features by processing tasks through Compound Engineering cycles with Ralph Wiggum for autonomous execution.

## Inputs Required
- Taskmaster tasks from Phase 3
- Architecture and design docs

## The Development Loop

For each task from Taskmaster:

### 1. PLAN (Compound Engineering)
```
/compound-engineering:plan based on task details
```
- Research codebase for existing patterns
- Check architecture docs for constraints
- Create implementation plan
- Define acceptance criteria

### 2. WORK (Compound Engineering)
```
/compound-engineering:work
```
- Create feature branch
- Implement code systematically
- Write tests as you go
- Run tests after each change
- Commit with clear messages

### 3. REVIEW (Compound Engineering)
```
/compound-engineering:review
```
- Run all review agents
- Fix critical issues
- Fix high-priority issues
- Re-run until clean

### 4. CODIFY (Compound Engineering)
- Document patterns learned
- Update project documentation
- Update CLAUDE.md if new conventions
- Mark task complete in Taskmaster

## Master Development Loop
```
/ralph-loop "
PHASE 4: DEVELOPMENT

Process all Taskmaster tasks:

LOOP until no more tasks:

1. GET NEXT TASK
   task-master next
   If no tasks, output completion promise

2. GET TASK DETAILS
   task-master show <task-id>
   Note dependencies and requirements

3. CREATE CHECKPOINT
   git tag forge-pre-task-<task-id>

4. COMPOUND ENGINEERING CYCLE

   4a. PLAN
   /compound-engineering:plan
   Create detailed implementation plan based on:
   - Task requirements
   - Architecture in sdlc/architecture.md
   - Security guidelines in sdlc/security-guidelines.md
   - Existing code patterns

   4b. WORK
   /compound-engineering:work
   - Create feature branch
   - Implement task requirements
   - Write tests (aim for >80% coverage of new code)
   - Run tests frequently
   - Commit after each logical change

   4c. REVIEW
   /compound-engineering:review
   - Run security review
   - Run code quality review
   - Fix all critical findings
   - Fix all high findings
   - Re-run until clean

   4d. CODIFY
   - Document any new patterns in docs/
   - Update CLAUDE.md if needed
   - Add learnings to task notes

5. COMPLETE TASK
   task-master set-status --id <task-id> --status done

6. MERGE
   Create PR or merge to develop branch

END LOOP

Output <promise>PHASE_4_COMPLETE</promise> when:
- task-master next returns no pending tasks
- All tests pass
- All PRs merged or ready
" --max-iterations 300 --completion-promise "PHASE_4_COMPLETE"
```

## Quality Gate Checklist
- [ ] All Taskmaster tasks complete
- [ ] Tests exist for all new code
- [ ] Test coverage meets threshold (80%)
- [ ] All tests passing
- [ ] Code reviewed and approved
- [ ] Documentation updated
- [ ] No critical security issues
