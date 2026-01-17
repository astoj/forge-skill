# Phase 3: Planning

## Objective
Break down the product into manageable tasks with dependencies, set up task management, and plan the development approach.

## Inputs Required
- PRD from Phase 1
- Architecture from Phase 2

## Activities

### 1. UI/UX Planning
- Create user flow diagrams
- Define UI patterns and components
- Document interaction guidelines
- Plan responsive behavior

### 2. Task Breakdown
- Initialize Taskmaster
- Parse PRD into tasks
- Analyze task complexity
- Expand complex tasks into subtasks

### 3. Dependency Mapping
- Identify task dependencies
- Ensure no circular dependencies
- Optimize task ordering
- Mark critical path

### 4. Milestone Planning
- Group tasks into milestones
- Set milestone dates
- Identify risks
- Plan contingencies

## Outputs
- `sdlc/app-flow.md`
- `sdlc/ui-ux.md`
- `.taskmaster/tasks/tasks.json`

## Ralph Loop
```
/ralph-loop "
PHASE 3: PLANNING

1. UI/UX DOCUMENTATION
   - Create user flow diagrams for main journeys
   - Document UI component patterns
   - Define interaction guidelines
   - Create sdlc/app-flow.md
   - Create sdlc/ui-ux.md

2. TASKMASTER SETUP
   - Initialize: task-master init
   - Parse PRD: task-master parse-prd sdlc/prd.md
   - Wait for tasks to generate

3. COMPLEXITY ANALYSIS
   - Run: task-master analyze-complexity
   - Identify tasks with score > 7
   - Expand complex tasks into subtasks

4. DEPENDENCY SETUP
   - Review task list
   - Set logical dependencies
   - Verify: task-master next returns valid task
   - Check no circular dependencies

5. VERIFICATION
   - List all tasks: task-master list
   - Confirm task count matches PRD scope
   - Ensure P0 features have tasks

Output <promise>PHASE_3_COMPLETE</promise> when:
- UI/UX docs created
- Taskmaster has tasks
- Dependencies set
- task-master next works
" --max-iterations 25 --completion-promise "PHASE_3_COMPLETE"
```

## Quality Gate Checklist
- [ ] User flows documented
- [ ] UI patterns defined
- [ ] Taskmaster initialized
- [ ] All features have tasks
- [ ] Task dependencies set
- [ ] Complex tasks broken down
- [ ] `task-master next` returns valid task
