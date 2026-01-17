# Phase 1: Discovery

## Objective
Transform a raw idea into a structured Product Requirements Document with clear problem definition, user personas, prioritized features, and success metrics.

## Inputs Required
- Problem statement or idea description
- Target audience (optional, will be developed)
- Competitive context (optional, will be researched)

## Activities

### 1. Problem Definition
- Clarify the core problem being solved
- Identify who experiences this problem
- Understand the impact of the problem
- Define what success looks like

### 2. User Research
- Create 2-3 detailed user personas
- Document user pain points
- Map user goals and motivations
- Identify user constraints

### 3. Competitive Analysis
- Research 3-5 competitors (use web search)
- Identify competitor strengths/weaknesses
- Find market gaps and opportunities
- Document differentiation strategy

### 4. Feature Definition
- Brainstorm all potential features
- Group features by category
- Prioritize using MoSCoW method:
  - **Must Have (P0)**: Critical for launch
  - **Should Have (P1)**: Important but not critical
  - **Could Have (P2)**: Nice to have
  - **Won't Have (P3)**: Future consideration

### 5. Success Metrics
- Define 3-5 key metrics
- Ensure metrics are measurable
- Set target values
- Define measurement method

## Outputs
- `sdlc/prd.md` - Complete PRD

## Ralph Loop
```
/ralph-loop "
PHASE 1: DISCOVERY

Execute discovery activities:

1. PROBLEM DEFINITION
   - Work with user to clarify problem statement
   - Document who experiences this problem
   - Quantify the impact if possible

2. USER PERSONAS (create 2-3)
   For each persona document:
   - Name and role
   - Demographics
   - Goals and motivations
   - Pain points
   - How they would use the product

3. COMPETITIVE ANALYSIS
   - Search web for top competitors
   - Document each competitor's approach
   - Identify gaps and opportunities

4. FEATURE PRIORITIZATION
   - List all features discussed
   - Categorize by MoSCoW
   - Ensure Must Haves are minimal viable

5. SUCCESS METRICS
   - Define 3-5 measurable KPIs
   - Set realistic targets

Create sdlc/prd.md using template from assets/templates/prd.md

Output <promise>PHASE_1_COMPLETE</promise> when PRD is complete and reviewed.
" --max-iterations 25 --completion-promise "PHASE_1_COMPLETE"
```

## Quality Gate Checklist
- [ ] Problem statement is clear and specific
- [ ] At least 2 user personas created
- [ ] Competitive analysis completed
- [ ] Features prioritized with MoSCoW
- [ ] P0 features are truly essential
- [ ] Success metrics are measurable
- [ ] User has reviewed and approved PRD
