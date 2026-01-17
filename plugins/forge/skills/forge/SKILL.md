---
name: forge
description: End-to-end product development from idea to production. Use when starting new projects, structuring existing code, or hardening production apps. Orchestrates Taskmaster MCP, Compound Engineering, and Ralph Wiggum for complete SDLC automation including PRD creation, architecture design, task planning, development loops, testing, CI/CD, deployment, monitoring, and maintenance. Triggers on: new project setup, adding structure to codebase, production hardening, SDLC documentation, overnight automation, project audits.
---

# Forge: End-to-End Product Development

Transform ideas into production-ready products with structured SDLC, automated development loops, and comprehensive quality gates.

## Quick Reference

| Command | Purpose |
|---------|---------|
| `forge:init` | Detect project state, recommend mode, initialize |
| `forge:inception` | Start new product from idea |
| `forge:accelerate` | Add structure to existing codebase |
| `forge:harden` | Production-harden deployed app |
| `forge:status` | Show current phase and progress |
| `forge:next` | Execute next recommended action |
| `forge:phase <N>` | Run specific phase (1-8) |
| `forge:audit` | Full product audit against standards |
| `forge:overnight` | Generate autonomous overnight script |
| `forge:docs` | Generate/sync SDLC documentation |

## Modes

### Inception Mode (0-20% maturity)
**For:** New ideas, greenfield projects
**Entry:** An idea, problem statement, or concept
**Process:** Full 8-phase journey from discovery to maintenance

### Acceleration Mode (20-80% maturity)
**For:** Existing codebases lacking structure
**Entry:** Working code without formal SDLC docs
**Process:** Audit gaps, generate missing docs, add automation

### Hardening Mode (80%+ maturity)
**For:** Production apps needing rigor
**Entry:** Deployed application with real users
**Process:** Security, reliability, observability hardening

## Phases

All modes progress through 8 phases (entry point varies by mode):

| # | Phase | Key Outputs |
|---|-------|-------------|
| 1 | Discovery | PRD, personas, success metrics |
| 2 | Architecture | System design, data model, security guidelines |
| 3 | Planning | Taskmaster tasks with dependencies |
| 4 | Development | Working code via Compound + Ralph loops |
| 5 | Quality | Tests, security scans, performance benchmarks |
| 6 | Deployment | CI/CD pipelines, environments, rollback |
| 7 | Observability | Monitoring, logging, alerting |
| 8 | Maintenance | Incident response, runbooks, tech debt tracking |

## Integration Stack

Forge orchestrates these tools:

- **Taskmaster MCP** - Task management with dependencies
- **Compound Engineering** - Plan, Work, Review, Codify loop
- **Ralph Wiggum** - Autonomous iteration until completion
- **Connected MCPs** - Database, cloud, Slack, etc.

## Instructions

### On `forge:init`

1. Run `scripts/init_project.py` to scan project directory
2. Check for existing files:
   - `sdlc/` folder and contents
   - `.taskmaster/` folder
   - Package managers (package.json, requirements.txt, etc.)
   - `.github/workflows/`
   - Test files and coverage
   - Deployment configs
3. Calculate maturity score (0-100%)
4. Recommend mode based on score:
   - 0-20%: Inception
   - 20-80%: Acceleration
   - 80-100%: Hardening
5. Present findings and await user confirmation
6. Create `forge.config.json` with initial state
7. Load appropriate mode file from [modes/](modes/)

### On `forge:inception`

1. Confirm user wants to start from scratch
2. Load [modes/inception.md](modes/inception.md)
3. Begin Phase 1: Discovery
4. Progress through all 8 phases sequentially
5. Use Ralph loops for autonomous execution where appropriate
6. Update `forge.config.json` after each phase

### On `forge:accelerate`

1. Load [modes/acceleration.md](modes/acceleration.md)
2. Run comprehensive audit
3. Generate gap report showing:
   - Missing SDLC documents
   - Missing tests
   - Missing CI/CD
   - Missing monitoring
4. Create Taskmaster tasks for remediation
5. Enter appropriate phase based on gaps

### On `forge:harden`

1. Load [modes/hardening.md](modes/hardening.md)
2. Run security audit
3. Check observability coverage
4. Verify incident response readiness
5. Generate hardening task list
6. Execute with Ralph loops

### On `forge:status`

1. Read `forge.config.json`
2. Display:
   - Current mode and phase
   - Phase progress (pending/in_progress/complete)
   - Integration status
   - Next recommended action
   - Blockers if any

### On `forge:next`

1. Read `forge.config.json` for current state
2. Determine next action based on phase and progress
3. Load appropriate phase file from [phases/](phases/)
4. Execute with Taskmaster + Compound + Ralph as needed
5. Update state after completion

### On `forge:phase <N>`

1. Validate phase number (1-8)
2. Load phase file: `phases/0N-phasename.md`
3. Execute phase workflow
4. Update `forge.config.json`

### On `forge:overnight`

1. Read `forge.config.json` for current state
2. Verify safety checks:
   - All tests currently passing
   - Git working directory clean
   - Checkpoint created
3. Generate overnight script with:
   - Ralph loops for remaining tasks
   - Max iteration limits
   - Completion promises
   - Safety gates
4. Output script for user to execute
5. See [references/ralph-prompts.md](references/ralph-prompts.md) for templates

### On `forge:docs`

1. Scan existing `sdlc/` folder
2. Compare against required documents
3. Generate missing documents from [assets/templates/](assets/templates/)
4. Update existing documents to sync with code state

### On `forge:audit`

1. Run full project audit:
   - SDLC document completeness
   - Code quality metrics
   - Test coverage
   - Security scan
   - Dependency check
   - Performance baseline
2. Generate audit report
3. Create remediation tasks in Taskmaster

## Quality Gates

Before phase transitions, validate:

| Transition | Requirements |
|------------|--------------|
| Discovery to Architecture | PRD complete with problem statement, personas defined, features prioritized |
| Architecture to Planning | All design docs present, security guidelines defined |
| Planning to Development | Tasks created in Taskmaster with dependencies |
| Development to Quality | All tasks complete, tests exist for new code |
| Quality to Deployment | Coverage threshold met, security scan clean |
| Deployment to Observability | CI/CD working, staging deployed successfully |
| Observability to Maintenance | Monitoring active, alerts configured, dashboards created |
| Maintenance to Complete | Runbooks documented, incident response tested |

## SDLC Document Structure

Forge creates/validates this structure in `sdlc/`:

```
sdlc/
├── prd.md                    # Product Requirements Document
├── architecture.md           # System architecture
├── app-flow.md               # User flows and journeys
├── ui-ux.md                  # UI/UX guidelines
├── security-guidelines.md    # Security requirements
├── test-documents.md         # Testing strategy
├── infrastructure.md         # Infrastructure design
├── cicd-pipeline.md          # CI/CD documentation
├── observability.md          # Monitoring strategy
├── incident-response.md      # Incident procedures
├── release-process.md        # Release management
├── maintenance.md            # Maintenance plan
├── tech-debt.md              # Technical debt tracking
└── runbooks/                 # Operational runbooks
    ├── deployment-rollback.md
    ├── database-issues.md
    ├── high-traffic.md
    └── third-party-outage.md
```

Templates available at [assets/templates/](assets/templates/).

## Safety Features

- **Git checkpoints**: Create tags before major operations
- **Rollback procedures**: Document how to undo changes
- **Max iterations**: Ralph loops have iteration limits
- **Human review gates**: Critical tasks require approval
- **Never auto-merge production**: PRs to main require human review

## Configuration

Forge stores state in `forge.config.json`:

```json
{
  "project_name": "My Product",
  "mode": "inception",
  "current_phase": 1,
  "phase_progress": {
    "discovery": "pending",
    "architecture": "pending",
    "planning": "pending",
    "development": "pending",
    "quality": "pending",
    "deployment": "pending",
    "observability": "pending",
    "maintenance": "pending"
  },
  "integrations": {
    "taskmaster": false,
    "compound_engineering": false,
    "ralph_wiggum": false
  },
  "quality_gates": {
    "test_coverage_threshold": 80,
    "require_security_scan": true,
    "require_review": true
  },
  "checkpoints": []
}
```

## Examples

**Start new project:**
```
User: "I have an idea for a SaaS app that helps restaurants manage inventory"
-> Forge activates, runs forge:init, recommends inception mode
-> Begins Phase 1: Discovery
```

**Add structure to existing code:**
```
User: "I have a working React app but no tests or docs"
-> Forge activates, runs forge:init, recommends acceleration mode
-> Audits gaps, generates remediation tasks
```

**Harden production app:**
```
User: "My app is live but I need better monitoring"
-> Forge activates, runs forge:init, recommends hardening mode
-> Runs observability audit, generates monitoring setup tasks
```

**Run overnight:**
```
User: "Run forge overnight to complete remaining tasks"
-> Forge generates overnight script with Ralph loops
-> User executes script, wakes up to completed work
```

## References

- [modes/inception.md](modes/inception.md) - Full inception workflow
- [modes/acceleration.md](modes/acceleration.md) - Acceleration workflow
- [modes/hardening.md](modes/hardening.md) - Hardening workflow
- [references/integrations.md](references/integrations.md) - Tool integration guide
- [references/quality-gates.md](references/quality-gates.md) - Quality gate details
- [references/ralph-prompts.md](references/ralph-prompts.md) - Ralph loop templates
- [phases/](phases/) - Individual phase workflows
- [assets/templates/](assets/templates/) - Document templates
