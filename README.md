# Forge - End-to-End Product Development

Transform ideas into production-ready products with structured SDLC, automated development loops, and comprehensive quality gates.

## What is Forge?

Forge is a Claude Code skill that orchestrates:
- **Taskmaster MCP** - Task management with dependencies
- **Compound Engineering** - Plan → Work → Review → Codify loop
- **Ralph Wiggum** - Autonomous iteration until completion

## Three Modes

| Mode | Maturity | Use When |
|------|----------|----------|
| **Inception** | 0-20% | Starting a new project from an idea |
| **Acceleration** | 20-80% | Adding structure to existing code |
| **Hardening** | 80%+ | Production-hardening a deployed app |

## Eight Phases

1. **Discovery** - PRD, personas, success metrics
2. **Architecture** - System design, data model, security
3. **Planning** - Taskmaster tasks with dependencies
4. **Development** - Working code via Compound + Ralph loops
5. **Quality** - Tests, security scans, performance
6. **Deployment** - CI/CD pipelines, environments
7. **Observability** - Monitoring, logging, alerting
8. **Maintenance** - Incident response, runbooks, tech debt

## Installation

### As a Plugin (Recommended)

```bash
# Add the marketplace
/plugin marketplace add astoj/forge-skill

# Install the plugin
/plugin install forge
```

### Manual Installation

Clone to your Claude Code skills directory:

```bash
git clone https://github.com/astoj/forge-skill ~/.claude/skills/forge
```

## Requirements

This skill requires these plugins to be installed:

- [Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin)
- [Ralph Wiggum](https://github.com/...) (Ralph loop plugin)
- [Taskmaster MCP](https://github.com/...) (Task management)

## Commands

| Command | Purpose |
|---------|---------|
| `forge:init` | Detect project state, recommend mode |
| `forge:inception` | Start new product from idea |
| `forge:accelerate` | Add structure to existing codebase |
| `forge:harden` | Production-harden deployed app |
| `forge:status` | Show current phase and progress |
| `forge:next` | Execute next recommended action |
| `forge:phase <N>` | Run specific phase (1-8) |
| `forge:audit` | Full product audit against standards |
| `forge:overnight` | Generate autonomous overnight script |
| `forge:docs` | Generate/sync SDLC documentation |

## Quick Start

1. Navigate to your project directory
2. Run `forge:init` to scan your project
3. Forge will recommend a mode based on maturity
4. Follow the guided workflow through all phases

## Example Usage

**Starting a new project:**
```
> I have an idea for a SaaS app that helps restaurants manage inventory

Forge activates → runs forge:init → recommends inception mode
→ Begins Phase 1: Discovery
```

**Adding structure to existing code:**
```
> I have a working React app but no tests or docs

Forge activates → runs forge:init → recommends acceleration mode
→ Audits gaps → generates remediation tasks
```

**Running overnight automation:**
```
> Run forge overnight to complete remaining tasks

Forge generates overnight script with Ralph loops
→ User executes script → wakes up to completed work
```

## File Structure

```
forge/
├── SKILL.md                    # Main entry point
├── modes/                      # Mode-specific workflows
├── phases/                     # Phase-specific workflows
├── references/                 # Integration guides
├── scripts/                    # Python utilities
└── assets/templates/           # SDLC document templates
```

## License

MIT License - See LICENSE file for details.

## Contributing

Contributions welcome! Please read CONTRIBUTING.md for guidelines.
