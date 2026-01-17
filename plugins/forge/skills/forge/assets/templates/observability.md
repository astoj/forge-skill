# Observability Strategy

## Three Pillars

### 1. Logs
- **Format:** JSON structured
- **Aggregation:** [CloudWatch / Datadog / ELK]
- **Retention:** 30 days

### 2. Metrics
- **Collection:** [Prometheus / CloudWatch]
- **Visualization:** [Grafana / CloudWatch Dashboards]
- **Retention:** 90 days

### 3. Traces
- **Provider:** [Jaeger / X-Ray / Datadog APM]
- **Sampling:** 10% of requests

---

## Health Endpoints

| Endpoint | Purpose | Response |
|----------|---------|----------|
| GET /health | Liveness check | 200 OK |
| GET /ready | Readiness check | 200 OK |
| GET /metrics | Prometheus metrics | Metrics data |

---

## Key Metrics

### Application Metrics
| Metric | Alert Threshold |
|--------|-----------------|
| Request rate | N/A (info) |
| Error rate | > 1% |
| Response time p95 | > 500ms |
| Active connections | > 1000 |

### Business Metrics
| Metric | Description |
|--------|-------------|
| User signups | New registrations |
| Active users | DAU/MAU |
| Feature usage | Feature adoption |

### Infrastructure Metrics
| Metric | Alert Threshold |
|--------|-----------------|
| CPU usage | > 80% |
| Memory usage | > 85% |
| Disk usage | > 90% |

---

## Alerting Rules

### Critical (P0)
- Service down
- Error rate > 10%
- Database unreachable

### High (P1)
- Error rate > 5%
- Response time p95 > 1s
- Disk usage > 90%

### Warning (P2)
- Error rate > 1%
- Response time p95 > 500ms
- Memory usage > 80%

---

## Dashboards

### Operations Dashboard
- Service health status
- Request/error rates
- Response times
- Resource utilization

### Business Dashboard
- User signups
- Active users
- Feature usage
- Revenue metrics

---

## Log Levels

| Level | Usage |
|-------|-------|
| ERROR | Errors requiring attention |
| WARN | Potential issues |
| INFO | Important events |
| DEBUG | Detailed debugging |

---

## On-Call

| Role | Responsibility |
|------|----------------|
| Primary | First responder |
| Secondary | Backup/escalation |
| Manager | Major incident coordinator |
