# Ralph Loop Prompt Templates

## Discovery Phase
```
/ralph-loop "
DISCOVERY PHASE for [PROJECT_NAME]:

1. Work with user to clarify:
   - Core problem being solved
   - Target users
   - Key differentiators

2. Create user personas (2-3):
   - Name, role, demographics
   - Goals and pain points
   - Usage scenarios

3. Research competitors:
   - Use web search for top 3-5
   - Document strengths/weaknesses
   - Identify opportunities

4. Feature prioritization:
   - List all features
   - Apply MoSCoW method
   - Ensure P0 is minimal viable

5. Success metrics:
   - Define 3-5 KPIs
   - Set measurable targets

Create sdlc/prd.md with all findings.

Output <promise>DISCOVERY_DONE</promise> when complete.
" --max-iterations 25 --completion-promise "DISCOVERY_DONE"
```

## Architecture Phase
```
/ralph-loop "
ARCHITECTURE PHASE:

Based on sdlc/prd.md:

1. Select technology stack:
   - Frontend: [recommend with rationale]
   - Backend: [recommend with rationale]
   - Database: [recommend with rationale]
   - Infrastructure: [recommend with rationale]

2. System design:
   - Create component diagram (mermaid)
   - Define responsibilities
   - Map data flow

3. Data model:
   - Entity relationship diagram
   - Schema definitions
   - Indexes and constraints

4. API design:
   - List endpoints
   - Request/response formats
   - Authentication approach

5. Security:
   - Auth mechanism
   - Data protection
   - Input validation

Create:
- sdlc/architecture.md
- sdlc/security-guidelines.md

Output <promise>ARCHITECTURE_DONE</promise>
" --max-iterations 30 --completion-promise "ARCHITECTURE_DONE"
```

## Development Task Loop
```
/ralph-loop "
DEVELOPMENT: Process task [TASK_ID]

1. Get details: task-master show [TASK_ID]

2. PLAN phase:
   /compound-engineering:plan based on task
   - Research codebase patterns
   - Check architecture constraints
   - Create implementation plan

3. WORK phase:
   /compound-engineering:work
   - Create feature branch
   - Implement requirements
   - Write tests (80% coverage)
   - Run tests frequently

4. REVIEW phase:
   /compound-engineering:review
   - Fix critical issues
   - Fix high issues
   - Re-run until clean

5. CODIFY phase:
   - Document patterns learned
   - Update docs if needed

6. Complete:
   task-master set-status --id [TASK_ID] --status done

Output <promise>TASK_[TASK_ID]_DONE</promise>
" --max-iterations 75 --completion-promise "TASK_[TASK_ID]_DONE"
```

## Quality Phase
```
/ralph-loop "
QUALITY PHASE:

1. Test coverage:
   - Run tests with coverage
   - Identify gaps
   - Add tests for uncovered paths
   - Target: 80% minimum

2. Integration tests:
   - Test API endpoints
   - Test component interactions
   - Test error scenarios

3. E2E tests:
   - Set up Playwright/Cypress
   - Test critical user flows
   - Run full suite

4. Security scan:
   - npm audit / pip-audit
   - Check dependencies
   - Fix vulnerabilities

5. Performance:
   - Run Lighthouse (frontend)
   - Load test APIs
   - Set budgets

Update sdlc/test-documents.md

Output <promise>QUALITY_DONE</promise> when:
- Coverage >= 80%
- All tests pass
- Security clean
" --max-iterations 50 --completion-promise "QUALITY_DONE"
```

## CI/CD Setup
```
/ralph-loop "
CI/CD SETUP:

1. Create .github/workflows/ci.yml:
   - Lint job
   - Test job
   - Security scan job
   - Build job
   - Deploy to staging (develop)
   - Deploy to production (main, manual)

2. Configure environments:
   - Development
   - Staging
   - Production

3. Set up secrets:
   - Document required secrets
   - Create .env.example

4. Test pipeline:
   - Push test commit
   - Verify all jobs pass
   - Test deployment

5. Document:
   - Create sdlc/cicd-pipeline.md
   - Document rollback procedure

Output <promise>CICD_DONE</promise>
" --max-iterations 40 --completion-promise "CICD_DONE"
```

## Overnight Full Pipeline
```
/ralph-loop "
OVERNIGHT PIPELINE:

Process all remaining Taskmaster tasks:

WHILE task-master next returns a task:

1. Get task: task-master next
2. Create checkpoint: git tag pre-task-$(date +%s)

3. Process with Compound Engineering:
   - Plan the implementation
   - Work on the code
   - Review changes
   - Fix issues
   - Codify learnings

4. Mark complete: task-master set-status --id <id> --status done

5. If stuck after 15 iterations on same task:
   - Document blockers in task notes
   - Mark as blocked
   - Continue to next task

END WHILE

After all tasks:
- Run full test suite
- Run security scan
- Generate summary report

Output <promise>OVERNIGHT_COMPLETE</promise>
" --max-iterations 500 --completion-promise "OVERNIGHT_COMPLETE"
```

## Hardening Security
```
/ralph-loop "
SECURITY HARDENING:

1. Dependency audit:
   - Run npm audit / pip-audit
   - Update vulnerable packages
   - Document exceptions

2. OWASP Top 10 check:
   - Injection prevention
   - Auth/session security
   - Sensitive data protection
   - Access control
   - Security config
   - XSS prevention
   - Insecure deserialization
   - Component vulnerabilities
   - Logging adequacy

3. Configuration review:
   - Security headers
   - CORS settings
   - Rate limiting
   - Input validation

4. Secrets audit:
   - Check for hardcoded secrets
   - Verify secrets management
   - Document rotation policy

Create sdlc/security-audit.md with findings.
Create remediation tasks in Taskmaster.

Output <promise>SECURITY_HARDENED</promise>
" --max-iterations 40 --completion-promise "SECURITY_HARDENED"
```
