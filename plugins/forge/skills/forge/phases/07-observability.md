# Phase 7: Observability

## Objective
Set up comprehensive monitoring, logging, alerting, and dashboards for production visibility.

## Activities

### 1. Health Endpoints
- Create /health endpoint
- Create /ready endpoint
- Add dependency health checks

### 2. Logging
- Implement structured logging
- Add correlation IDs
- Configure log levels
- Set up log aggregation

### 3. Metrics
- Add application metrics
- Add business metrics
- Configure metrics collection

### 4. Alerting
- Define alert thresholds
- Configure notification channels
- Set up escalation

### 5. Dashboards
- Create operational dashboard
- Create business metrics dashboard

## Outputs
- `sdlc/observability.md`
- Health endpoints in code
- Dashboards configured

## Ralph Loop
```
/ralph-loop "
PHASE 7: OBSERVABILITY

1. HEALTH ENDPOINTS
   Add to application:
   - GET /health - returns 200 if alive
   - GET /ready - returns 200 if ready to serve
   - Include dependency checks (DB, cache, etc.)

2. STRUCTURED LOGGING
   - Use JSON log format
   - Include: timestamp, level, message, correlation_id
   - Add request context logging
   - Configure log levels per environment

3. APPLICATION METRICS
   Add metrics for:
   - Request count by endpoint
   - Response time percentiles
   - Error rates
   - Active connections
   - Queue depths (if applicable)

4. BUSINESS METRICS
   Track key business events:
   - User signups
   - Feature usage
   - Conversions
   - Errors by type

5. ALERTING
   Configure alerts for:
   - Error rate > threshold
   - Response time > threshold
   - Health check failures
   - Resource usage (CPU, memory)

6. DASHBOARDS
   Create dashboards showing:
   - System health overview
   - Request/error trends
   - Performance metrics
   - Business metrics

7. DOCUMENTATION
   Create sdlc/observability.md with:
   - Monitoring architecture
   - Alert definitions
   - Dashboard locations
   - On-call procedures

Output <promise>PHASE_7_COMPLETE</promise> when:
- Health endpoints working
- Logging configured
- Metrics collecting
- Alerts set up
- Dashboards created
" --max-iterations 35 --completion-promise "PHASE_7_COMPLETE"
```

## Quality Gate Checklist
- [ ] Health endpoints implemented
- [ ] Structured logging in place
- [ ] Metrics being collected
- [ ] Alerts configured
- [ ] Dashboards created
- [ ] On-call rotation defined
- [ ] Documentation complete
