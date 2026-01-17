# Inception Mode: Idea to Launch

## Overview

Inception mode takes a raw idea and transforms it into a production-ready product through all 8 phases.

**Entry requirements:** An idea, problem statement, or concept
**Exit criteria:** Deployed, monitored, and maintained product

## Phase Flow

```
Idea -> Discovery -> Architecture -> Planning -> Development ->
Quality -> Deployment -> Observability -> Maintenance -> Launch
```

## Phase 1: Discovery

### Inputs
- Problem statement or idea description
- Target user/customer (optional, will be developed)
- Competitive context (optional, will be researched)

### Activities
1. Refine problem statement with user
2. Develop 2-3 user personas
3. Research competitors (use web search)
4. Brainstorm features
5. Prioritize using MoSCoW method
6. Define success metrics and KPIs

### Outputs
- `sdlc/prd.md` - Product Requirements Document
- `sdlc/user-personas.md` - Target user profiles (optional, can be in PRD)
- `sdlc/success-metrics.md` - KPIs and goals (optional, can be in PRD)

### Ralph Loop Template
```
/ralph-loop "
Complete Discovery Phase:

1. Clarify problem statement with user if needed
2. Create 2-3 detailed user personas
3. Research top 3-5 competitors using web search
4. List all potential features
5. Prioritize features using MoSCoW (Must/Should/Could/Won't)
6. Define 3-5 measurable success metrics

Create sdlc/prd.md with all findings.
Use template from assets/templates/prd.md

Output <promise>DISCOVERY_COMPLETE</promise> when:
- PRD exists with clear problem statement
- At least 2 personas defined
- Features prioritized
- Success metrics are measurable
" --max-iterations 20 --completion-promise "DISCOVERY_COMPLETE"
```

### Quality Gate
- [ ] PRD has clear problem statement
- [ ] At least 2 user personas defined
- [ ] Features prioritized with MoSCoW
- [ ] Success metrics are measurable
- [ ] Competitive analysis included

---

## Phase 2: Architecture

### Inputs
- Completed PRD from Phase 1

### Activities
1. Select technology stack
2. Design system architecture
3. Create data model
4. Design API contracts
5. Define security architecture
6. Plan infrastructure

### Outputs
- `sdlc/architecture.md` - System architecture
- `sdlc/security-guidelines.md` - Security requirements
- `sdlc/infrastructure.md` - Infrastructure plan (optional)

### Ralph Loop Template
```
/ralph-loop "
Complete Architecture Phase:

Based on sdlc/prd.md:

1. Recommend technology stack with justification
2. Create system architecture diagram (mermaid)
3. Design data model with entity relationships
4. Define API contracts (REST/GraphQL endpoints)
5. Document security requirements:
   - Authentication/authorization
   - Data protection
   - Input validation
   - Security headers
6. Plan infrastructure (cloud provider, services)

Create:
- sdlc/architecture.md
- sdlc/security-guidelines.md

Use templates from assets/templates/

Output <promise>ARCHITECTURE_COMPLETE</promise> when:
- Tech stack selected and justified
- Architecture diagram exists
- Data model defined
- Security guidelines documented
" --max-iterations 25 --completion-promise "ARCHITECTURE_COMPLETE"
```

### Quality Gate
- [ ] Technology stack selected with rationale
- [ ] System architecture documented with diagram
- [ ] Data model defined
- [ ] API contracts specified
- [ ] Security requirements documented
- [ ] Infrastructure planned

---

## Phase 3: Planning

### Inputs
- PRD and Architecture docs

### Activities
1. Create UI/UX wireframes and flows
2. Break down features into tasks
3. Set up Taskmaster
4. Create tasks with dependencies
5. Estimate complexity
6. Plan milestones

### Outputs
- `sdlc/app-flow.md` - User journeys
- `sdlc/ui-ux.md` - UI/UX guidelines
- `.taskmaster/tasks/tasks.json` - Task breakdown

### Ralph Loop Template
```
/ralph-loop "
Complete Planning Phase:

1. Create user flow diagrams for main journeys
2. Document UI/UX guidelines and patterns
3. Initialize Taskmaster: task-master init
4. Parse PRD into tasks: task-master parse-prd sdlc/prd.md
5. Analyze complexity: task-master analyze-complexity
6. Expand high-complexity tasks (score > 7)
7. Set task dependencies
8. Verify no circular dependencies

Create:
- sdlc/app-flow.md
- sdlc/ui-ux.md

Output <promise>PLANNING_COMPLETE</promise> when:
- App flows documented
- UI/UX guidelines exist
- Taskmaster initialized with tasks
- Dependencies set correctly
- task-master next returns a valid task
" --max-iterations 25 --completion-promise "PLANNING_COMPLETE"
```

### Quality Gate
- [ ] User flows documented
- [ ] UI/UX guidelines defined
- [ ] Taskmaster initialized
- [ ] Tasks created with dependencies
- [ ] Complexity analyzed
- [ ] First task ready to work

---

## Phase 4: Development

### Inputs
- Taskmaster tasks ready
- Architecture and design docs

### Activities
1. Process tasks in dependency order
2. Use Compound Engineering for each task
3. Use Ralph loops for autonomous work
4. Maintain test coverage
5. Document as you go

### Outputs
- Working code
- Tests for all features
- Updated documentation

### Master Development Loop
```
/ralph-loop "
DEVELOPMENT PHASE - Process all tasks:

REPEAT until task-master next returns no tasks:

1. Get next task: task-master next
2. For each task, run Compound Engineering cycle:

   PLAN:
   /compound-engineering:plan based on task details
   - Research codebase for patterns
   - Create implementation plan

   WORK:
   /compound-engineering:work on the plan
   - Create feature branch
   - Implement systematically
   - Write tests
   - Run tests after each change

   REVIEW:
   /compound-engineering:review
   - Run all review agents
   - Fix critical/high issues
   - Re-run until clean

   CODIFY:
   - Document patterns learned
   - Update CLAUDE.md if needed
   - Mark task done: task-master set-status --id <id> --status done

3. Create checkpoint: git tag forge-checkpoint-<timestamp>

Output <promise>DEVELOPMENT_COMPLETE</promise> when:
- task-master next returns no pending tasks
- All tests pass
- No critical issues in reviews
" --max-iterations 200 --completion-promise "DEVELOPMENT_COMPLETE"
```

### Quality Gate
- [ ] All Taskmaster tasks complete
- [ ] Tests exist for new code
- [ ] All tests passing
- [ ] Code reviewed
- [ ] Documentation updated

---

## Phases 5-8

Continue to Phase 5 (Quality), Phase 6 (Deployment), Phase 7 (Observability), and Phase 8 (Maintenance) following the same pattern.

See individual phase files in `phases/` for detailed workflows.
