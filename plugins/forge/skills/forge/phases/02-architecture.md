# Phase 2: Architecture

## Objective
Design the technical architecture including system design, data model, API contracts, security requirements, and infrastructure plan.

## Inputs Required
- Completed PRD from Phase 1

## Activities

### 1. Technology Stack Selection
- Evaluate options based on:
  - Team expertise
  - Scalability requirements
  - Cost considerations
  - Ecosystem and community
- Document selection rationale

### 2. System Architecture
- Design high-level architecture
- Define component responsibilities
- Map data flow between components
- Create architecture diagram (mermaid)

### 3. Data Model Design
- Identify entities and relationships
- Design database schema
- Document data types and constraints
- Consider data migration needs

### 4. API Contract Design
- Define API endpoints
- Specify request/response formats
- Document authentication requirements
- Create OpenAPI spec if REST

### 5. Security Architecture
- Authentication mechanism
- Authorization model
- Data encryption (at rest, in transit)
- Input validation strategy
- Security headers

### 6. Infrastructure Planning
- Cloud provider selection
- Service architecture
- Scaling strategy
- Cost estimation

## Outputs
- `sdlc/architecture.md`
- `sdlc/security-guidelines.md`
- `sdlc/infrastructure.md` (optional)

## Ralph Loop
```
/ralph-loop "
PHASE 2: ARCHITECTURE

Based on sdlc/prd.md, design technical architecture:

1. TECHNOLOGY STACK
   Recommend and justify:
   - Frontend framework
   - Backend language/framework
   - Database
   - Cache (if needed)
   - Message queue (if needed)
   - Cloud provider

2. SYSTEM ARCHITECTURE
   - Create component diagram (mermaid)
   - Define responsibilities per component
   - Map data flow
   - Identify integration points

3. DATA MODEL
   - Design entity relationship diagram
   - Define schema for each entity
   - Document relationships
   - Consider indexes and constraints

4. API CONTRACTS
   - List all endpoints
   - Define request/response schemas
   - Document authentication
   - Specify error formats

5. SECURITY
   - Authentication strategy (JWT, OAuth, etc.)
   - Authorization model (RBAC, ABAC)
   - Data protection requirements
   - Input validation rules
   - Security headers to implement

6. INFRASTRUCTURE
   - Cloud services needed
   - Environment strategy (dev/staging/prod)
   - Scaling approach
   - Estimated costs

Create:
- sdlc/architecture.md
- sdlc/security-guidelines.md

Use templates from assets/templates/

Output <promise>PHASE_2_COMPLETE</promise> when architecture is documented.
" --max-iterations 30 --completion-promise "PHASE_2_COMPLETE"
```

## Quality Gate Checklist
- [ ] Tech stack selected with rationale
- [ ] Architecture diagram created
- [ ] Data model designed
- [ ] API contracts defined
- [ ] Security requirements documented
- [ ] Infrastructure planned
- [ ] User has reviewed architecture
