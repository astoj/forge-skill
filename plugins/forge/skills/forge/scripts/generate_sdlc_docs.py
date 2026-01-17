#!/usr/bin/env python3
"""
Generate missing SDLC documents from templates.
"""

import os
import sys
import shutil
from pathlib import Path


def get_skill_path() -> Path:
    """Get the path to the Forge skill directory."""
    # Check common locations
    locations = [
        Path.home() / ".claude" / "skills" / "forge",
        Path(".claude") / "skills" / "forge",
    ]

    for loc in locations:
        if loc.exists():
            return loc

    raise FileNotFoundError("Forge skill directory not found")


def generate_docs(project_path: str = ".", docs_to_generate: list = None):
    """Generate missing SDLC documents."""

    project = Path(project_path).resolve()
    sdlc_path = project / "sdlc"

    # Create sdlc folder if it doesn't exist
    sdlc_path.mkdir(exist_ok=True)

    # Get template path
    try:
        skill_path = get_skill_path()
        templates_path = skill_path / "assets" / "templates"
    except FileNotFoundError:
        print("Error: Forge skill templates not found")
        sys.exit(1)

    # All available templates
    all_templates = [
        "prd.md",
        "architecture.md",
        "app-flow.md",
        "ui-ux.md",
        "security-guidelines.md",
        "test-documents.md",
        "infrastructure.md",
        "cicd-pipeline.md",
        "observability.md",
        "incident-response.md",
        "release-process.md",
        "maintenance.md"
    ]

    # Determine which docs to generate
    if docs_to_generate is None:
        # Generate all missing docs
        existing = [f.name for f in sdlc_path.glob("*.md")]
        docs_to_generate = [d for d in all_templates if d not in existing]

    # Generate each document
    generated = []
    for doc in docs_to_generate:
        template_file = templates_path / doc
        output_file = sdlc_path / doc

        if output_file.exists():
            print(f"Skipping {doc} (already exists)")
            continue

        if template_file.exists():
            shutil.copy(template_file, output_file)
            print(f"Generated {doc}")
            generated.append(doc)
        else:
            print(f"Warning: Template not found for {doc}")

    # Create runbooks folder
    runbooks_path = sdlc_path / "runbooks"
    if not runbooks_path.exists():
        runbooks_path.mkdir()
        print("Created runbooks/ directory")

    print(f"\nGenerated {len(generated)} documents")
    return generated


if __name__ == "__main__":
    project_path = sys.argv[1] if len(sys.argv) > 1 else "."
    docs = sys.argv[2:] if len(sys.argv) > 2 else None

    generate_docs(project_path, docs)
