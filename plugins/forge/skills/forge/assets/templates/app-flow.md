# Application Flow

## User Journeys

### Journey 1: [Name]
**Actor:** [User type]
**Goal:** [What they want to accomplish]

```mermaid
graph LR
    A[Start] --> B[Step 1]
    B --> C[Step 2]
    C --> D[Step 3]
    D --> E[End]
```

**Steps:**
1. [Step description]
2. [Step description]
3. [Step description]

**Success Criteria:**
- [Criterion 1]
- [Criterion 2]

---

### Journey 2: [Name]
**Actor:** [User type]
**Goal:** [What they want to accomplish]

```mermaid
graph LR
    A[Start] --> B[Step 1]
    B --> C{Decision}
    C -->|Yes| D[Path A]
    C -->|No| E[Path B]
    D --> F[End]
    E --> F
```

---

## Screen Flow

```mermaid
graph TD
    Landing[Landing Page] --> Login[Login]
    Landing --> Signup[Signup]
    Login --> Dashboard[Dashboard]
    Signup --> Onboarding[Onboarding]
    Onboarding --> Dashboard
    Dashboard --> Feature1[Feature 1]
    Dashboard --> Feature2[Feature 2]
    Dashboard --> Settings[Settings]
```

---

## State Diagram

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Loading: User action
    Loading --> Success: Data loaded
    Loading --> Error: Request failed
    Success --> Idle: Reset
    Error --> Idle: Retry
```

---

## Error Flows

### [Error Type 1]
**Trigger:** [What causes this]
**User Experience:** [What user sees]
**Recovery:** [How to recover]
