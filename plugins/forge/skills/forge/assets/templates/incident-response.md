# Incident Response Plan

## Severity Levels

| Level | Description | Response Time | Examples |
|-------|-------------|---------------|----------|
| P0 | Complete outage | 15 minutes | Service down |
| P1 | Major impact | 30 minutes | Key feature broken |
| P2 | Minor impact | 4 hours | Non-critical bug |
| P3 | Low impact | 24 hours | Cosmetic issues |

## Response Procedures

### P0/P1 Incidents
1. Acknowledge incident
2. Assess impact
3. Communicate status
4. Implement fix or rollback
5. Verify resolution
6. Post-mortem within 48h

## Communication Templates

### Initial
> [INCIDENT] [Severity] - [Brief description]
> Status: Investigating
> Impact: [Who/what affected]
> Next update: [Time]

### Resolution
> [RESOLVED] [Brief description]
> Duration: [Start - End]
> Impact: [Summary]
> Root cause: [Brief]

## Escalation Path
1. On-call engineer
2. Team lead
3. Engineering manager
4. VP Engineering

## Post-Mortem Template
- Timeline of events
- Root cause analysis
- Impact assessment
- Action items
- Lessons learned

## On-Call Schedule
| Week | Primary | Secondary |
|------|---------|-----------|
| [Date] | [Name] | [Name] |
