# Phase 5: Quality

## Objective
Ensure comprehensive test coverage, security scanning, and performance validation before deployment.

## Activities

### 1. Test Coverage
- Verify unit test coverage
- Add integration tests
- Create E2E tests for critical paths
- Run full test suite

### 2. Security Scanning
- Run SAST (static analysis)
- Run dependency vulnerability scan
- Review security configurations
- Penetration testing (if applicable)

### 3. Performance Testing
- Run load tests
- Measure response times
- Identify bottlenecks
- Set performance budgets

### 4. Accessibility Testing
- Run accessibility audit
- Fix WCAG violations
- Test with screen readers

## Outputs
- `sdlc/test-documents.md` (updated)
- Test reports
- Security scan results
- Performance benchmarks

## Ralph Loop
```
/ralph-loop "
PHASE 5: QUALITY

1. TEST COVERAGE ANALYSIS
   - Run test suite with coverage
   - Identify uncovered code paths
   - Add tests for critical uncovered paths
   - Target: 80% coverage minimum

2. INTEGRATION TESTS
   - Test component interactions
   - Test API endpoints
   - Test database operations
   - Test external integrations

3. E2E TESTS
   - Set up Playwright or Cypress
   - Test critical user journeys:
     - User registration/login
     - Main feature flows
     - Error scenarios
   - Run E2E suite

4. SECURITY SCANNING
   - Run npm audit / pip-audit
   - Run SAST tool if available
   - Check OWASP Top 10
   - Document findings

5. PERFORMANCE TESTING
   - Run Lighthouse for frontend
   - Load test critical endpoints
   - Set performance budgets
   - Document benchmarks

6. DOCUMENTATION
   - Update sdlc/test-documents.md
   - Document test strategy
   - Record coverage metrics
   - List known issues

Output <promise>PHASE_5_COMPLETE</promise> when:
- Coverage >= 80%
- All tests passing
- Security scan clean (no critical/high)
- Performance benchmarks set
" --max-iterations 50 --completion-promise "PHASE_5_COMPLETE"
```

## Quality Gate Checklist
- [ ] Unit test coverage >= 80%
- [ ] Integration tests passing
- [ ] E2E tests for critical paths
- [ ] Security scan clean
- [ ] No critical vulnerabilities
- [ ] Performance benchmarks met
- [ ] Accessibility audit passed
