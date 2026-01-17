# Phase 6: Deployment

## Objective
Set up CI/CD pipelines, configure environments, and deploy to staging/production with rollback capability.

## Activities

### 1. CI/CD Pipeline
- Create workflow configuration
- Set up build step
- Configure test automation
- Add security scanning
- Set up deployment steps

### 2. Environment Configuration
- Configure development environment
- Set up staging environment
- Configure production environment
- Manage secrets

### 3. Database Migrations
- Create migration scripts
- Test migrations
- Document rollback procedures

### 4. Deployment Execution
- Deploy to staging
- Run smoke tests
- Deploy to production
- Verify deployment

## Outputs
- `.github/workflows/ci.yml` (or equivalent)
- `sdlc/cicd-pipeline.md`
- `sdlc/deployment.md`

## Ralph Loop
```
/ralph-loop "
PHASE 6: DEPLOYMENT

1. CI/CD PIPELINE
   Create .github/workflows/ci.yml with:
   - Trigger: push to main/develop, PRs to main
   - Jobs:
     - Lint
     - Unit tests
     - Integration tests
     - Security scan
     - Build
     - Deploy to staging (develop branch)
     - Deploy to production (main branch, manual approval)

2. ENVIRONMENT SETUP
   - Document environment variables
   - Create .env.example
   - Configure secrets in CI/CD
   - Set up staging environment
   - Prepare production environment

3. DATABASE MIGRATIONS
   - Ensure migration scripts exist
   - Test migrations on staging
   - Document rollback procedures

4. STAGING DEPLOYMENT
   - Deploy to staging
   - Run smoke tests
   - Verify all features work
   - Fix any issues

5. DOCUMENTATION
   - Create sdlc/cicd-pipeline.md
   - Document deployment procedures
   - Document rollback steps

Output <promise>PHASE_6_COMPLETE</promise> when:
- CI/CD pipeline working
- Staging deployed and verified
- Documentation complete
" --max-iterations 40 --completion-promise "PHASE_6_COMPLETE"
```

## Quality Gate Checklist
- [ ] CI/CD pipeline created and working
- [ ] All environments configured
- [ ] Secrets properly managed
- [ ] Staging deployment successful
- [ ] Smoke tests passing
- [ ] Rollback procedure documented and tested
- [ ] Deployment documentation complete
