# Acceleration Mode: Add Structure to Existing Code

## Overview

Acceleration mode takes an existing codebase and adds proper SDLC structure, documentation, tests, and automation.

**Entry requirements:** Working code without formal structure
**Exit criteria:** Fully structured project with documentation and automation

## Initial Audit

Run comprehensive audit to identify gaps:

```
/ralph-loop "
ACCELERATION AUDIT:

1. Scan project structure:
   - Identify tech stack from package files
   - Count source files by type
   - Check for existing tests
   - Look for CI/CD configs
   - Find existing documentation

2. Check SDLC folder:
   - List existing sdlc/*.md files
   - Identify missing documents

3. Check Taskmaster:
   - Does .taskmaster/ exist?
   - Are there tasks defined?

4. Check quality:
   - Run existing tests if any
   - Check test coverage if available
   - Run linter if configured

5. Generate gap report:
   - Missing SDLC documents (list each)
   - Missing tests (estimate coverage)
   - Missing CI/CD
   - Missing monitoring
   - Security concerns

6. Calculate maturity score (0-100)

Output findings as JSON and recommend entry phase.

Output <promise>AUDIT_COMPLETE</promise>
" --max-iterations 15 --completion-promise "AUDIT_COMPLETE"
```

## Gap Remediation Strategy

Based on audit, create remediation tasks:

### Missing Documentation
For each missing SDLC document:
1. Reverse-engineer from existing code
2. Use templates from assets/templates/
3. Have user review and refine

### Missing Tests
1. Identify critical paths
2. Create test plan
3. Generate tests for existing code
4. Set coverage targets

### Missing CI/CD
1. Generate workflow from templates
2. Configure for detected tech stack
3. Set up environments

### Missing Monitoring
1. Add health endpoints
2. Configure logging
3. Set up basic metrics

## Phase Entry Points

Based on audit results, enter at appropriate phase:

| Current State | Entry Phase |
|---------------|-------------|
| No docs at all | Phase 1: Discovery (reverse-engineer PRD) |
| Docs but no tasks | Phase 3: Planning |
| Tasks but incomplete | Phase 4: Development |
| Complete but untested | Phase 5: Quality |
| Tested but not deployed | Phase 6: Deployment |
| Deployed but not monitored | Phase 7: Observability |

## Reverse Engineering Commands

### Generate PRD from code
```
/ralph-loop "
Reverse-engineer PRD from existing codebase:

1. Analyze code structure and features
2. Identify user-facing functionality
3. Infer problem being solved
4. Document current features as requirements
5. Create sdlc/prd.md

Mark features as 'implemented' vs 'planned'.

Output <promise>PRD_GENERATED</promise>
" --max-iterations 20 --completion-promise "PRD_GENERATED"
```

### Generate architecture from code
```
/ralph-loop "
Document architecture from existing code:

1. Identify components and their relationships
2. Map data flow between components
3. Document current tech stack
4. Create architecture diagram
5. Note any technical debt observed
6. Create sdlc/architecture.md

Output <promise>ARCHITECTURE_DOCUMENTED</promise>
" --max-iterations 20 --completion-promise "ARCHITECTURE_DOCUMENTED"
```
