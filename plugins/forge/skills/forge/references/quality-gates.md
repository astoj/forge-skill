# Quality Gates

## Phase Transition Gates

### Discovery to Architecture
**Required:**
- [ ] PRD exists at `sdlc/prd.md`
- [ ] Problem statement is clear and specific
- [ ] At least 2 user personas defined
- [ ] Features listed and prioritized (MoSCoW)
- [ ] Success metrics are measurable

**Validation:**
```bash
# Check PRD exists and has content
test -f sdlc/prd.md && [ $(wc -l < sdlc/prd.md) -gt 50 ]
```

### Architecture to Planning
**Required:**
- [ ] Architecture doc at `sdlc/architecture.md`
- [ ] Tech stack selected with rationale
- [ ] System diagram exists (mermaid or image)
- [ ] Data model defined
- [ ] Security guidelines at `sdlc/security-guidelines.md`

**Validation:**
```bash
test -f sdlc/architecture.md && test -f sdlc/security-guidelines.md
```

### Planning to Development
**Required:**
- [ ] Taskmaster initialized (`.taskmaster/` exists)
- [ ] Tasks created (`tasks.json` has entries)
- [ ] `task-master next` returns a valid task
- [ ] UI/UX docs exist

**Validation:**
```bash
test -d .taskmaster && task-master next
```

### Development to Quality
**Required:**
- [ ] All Taskmaster tasks marked `done`
- [ ] Tests exist for new code
- [ ] All tests passing
- [ ] No uncommitted changes

**Validation:**
```bash
# No pending tasks
[ $(task-master list --status pending --count) -eq 0 ]
# Tests pass
npm test || pytest || cargo test
```

### Quality to Deployment
**Required:**
- [ ] Test coverage >= 80%
- [ ] Security scan clean (no critical/high)
- [ ] E2E tests passing
- [ ] Performance benchmarks documented

**Validation:**
```bash
# Coverage check (example for Jest)
npm run test:coverage -- --coverageThreshold='{"global":{"lines":80}}'
# Security scan
npm audit --audit-level=high
```

### Deployment to Observability
**Required:**
- [ ] CI/CD pipeline working
- [ ] Staging deployment successful
- [ ] Smoke tests passing
- [ ] Rollback tested

**Validation:**
```bash
# CI/CD exists
test -f .github/workflows/ci.yml
# Health check passes
curl -f http://staging.example.com/health
```

### Observability to Maintenance
**Required:**
- [ ] Health endpoints responding
- [ ] Logging configured
- [ ] Metrics collecting
- [ ] Alerts configured
- [ ] Dashboard created

**Validation:**
```bash
curl -f http://production.example.com/health
curl -f http://production.example.com/ready
```

### Maintenance to Complete
**Required:**
- [ ] Incident response documented
- [ ] Runbooks created
- [ ] Release process defined
- [ ] Tech debt tracked

**Validation:**
```bash
test -f sdlc/incident-response.md
test -d sdlc/runbooks
test -f sdlc/release-process.md
```

---

## Code Quality Standards

### Test Coverage
- Minimum: 80% line coverage
- Critical paths: 100% coverage
- New code: Must have tests

### Security
- No critical vulnerabilities
- No high vulnerabilities
- Dependencies up to date
- Secrets not in code

### Performance
- API response time < 200ms p95
- Page load < 3s
- Core Web Vitals passing

### Documentation
- README complete
- API documented
- CHANGELOG maintained
- Architecture current
