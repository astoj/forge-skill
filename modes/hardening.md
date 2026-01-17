# Hardening Mode: Production-Grade Rigor

## Overview

Hardening mode takes a deployed application and adds production-grade security, reliability, and observability.

**Entry requirements:** Deployed application with real users
**Exit criteria:** Battle-tested product ready for scale

## Hardening Checklist

### Security Hardening
- [ ] Penetration test completed
- [ ] OWASP Top 10 addressed
- [ ] Dependency vulnerabilities patched
- [ ] Secrets rotated and vaulted
- [ ] WAF/DDoS protection enabled
- [ ] Security headers configured
- [ ] Input validation comprehensive
- [ ] Output encoding in place
- [ ] CORS properly configured
- [ ] Rate limiting implemented

### Reliability Hardening
- [ ] 99.9% uptime architecture designed
- [ ] Auto-scaling configured
- [ ] Database failover tested
- [ ] Backup/restore verified
- [ ] Disaster recovery plan documented
- [ ] Load testing completed
- [ ] Circuit breakers implemented
- [ ] Graceful degradation planned
- [ ] Health checks comprehensive
- [ ] Connection pooling optimized

### Observability Hardening
- [ ] APM with distributed tracing
- [ ] Structured logging (JSON)
- [ ] Log aggregation configured
- [ ] Error tracking (Sentry, etc.)
- [ ] Real user monitoring
- [ ] Synthetic monitoring
- [ ] Custom dashboards created
- [ ] SLOs/SLAs defined
- [ ] Alerting rules comprehensive
- [ ] On-call rotation established

### Operational Hardening
- [ ] Runbooks for all critical paths
- [ ] Incident response plan tested
- [ ] Post-mortem process defined
- [ ] Change management documented
- [ ] Rollback procedures verified
- [ ] Communication plan ready
- [ ] Status page configured
- [ ] Documentation complete
- [ ] Team trained
- [ ] Compliance verified (if applicable)

## Security Audit Loop

```
/ralph-loop "
SECURITY HARDENING:

1. Run security scan (use available tools)
2. Check OWASP Top 10:
   - Injection vulnerabilities
   - Broken authentication
   - Sensitive data exposure
   - XML external entities
   - Broken access control
   - Security misconfiguration
   - XSS
   - Insecure deserialization
   - Known vulnerabilities
   - Insufficient logging

3. Scan dependencies:
   - npm audit / pip-audit / etc.
   - Update vulnerable packages

4. Check configurations:
   - Security headers
   - CORS settings
   - Rate limiting
   - Input validation

5. Document findings in sdlc/security-audit.md
6. Create remediation tasks in Taskmaster

Output <promise>SECURITY_AUDIT_COMPLETE</promise>
" --max-iterations 30 --completion-promise "SECURITY_AUDIT_COMPLETE"
```

## Observability Setup Loop

```
/ralph-loop "
OBSERVABILITY HARDENING:

1. Health endpoints:
   - /health for liveness
   - /ready for readiness
   - Dependency health checks

2. Logging:
   - Ensure structured JSON logging
   - Add correlation IDs
   - Configure log levels
   - Set up log aggregation

3. Metrics:
   - Application metrics
   - Business metrics
   - Infrastructure metrics

4. Alerting:
   - Define alert thresholds
   - Configure notification channels
   - Create escalation policies

5. Dashboards:
   - Create operational dashboard
   - Create business metrics dashboard

6. Document in sdlc/observability.md

Output <promise>OBSERVABILITY_COMPLETE</promise>
" --max-iterations 30 --completion-promise "OBSERVABILITY_COMPLETE"
```

## Incident Response Setup

```
/ralph-loop "
INCIDENT RESPONSE SETUP:

1. Create severity definitions (P0-P3)
2. Define response procedures per severity
3. Create communication templates
4. Set up status page
5. Document escalation paths
6. Create runbooks for common issues:
   - Database issues
   - High traffic/load
   - Third-party outages
   - Deployment failures
   - Security incidents
7. Document post-mortem template
8. Create sdlc/incident-response.md
9. Create sdlc/runbooks/*.md

Output <promise>INCIDENT_RESPONSE_READY</promise>
" --max-iterations 25 --completion-promise "INCIDENT_RESPONSE_READY"
```
