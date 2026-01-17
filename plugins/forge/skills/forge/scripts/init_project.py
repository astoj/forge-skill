#!/usr/bin/env python3
"""
Initialize Forge for a project.
Scans project structure and recommends appropriate mode.
"""

import os
import json
import sys
from pathlib import Path
from datetime import datetime


def scan_project(project_path: str = ".") -> dict:
    """Scan project and determine maturity level."""

    path = Path(project_path).resolve()

    findings = {
        "project_path": str(path),
        "project_name": path.name,
        "scan_time": datetime.now().isoformat(),

        # SDLC Documentation
        "has_sdlc_folder": False,
        "sdlc_docs": [],
        "missing_sdlc_docs": [],

        # Task Management
        "has_taskmaster": False,
        "taskmaster_task_count": 0,

        # Code
        "has_code": False,
        "code_files_count": 0,
        "detected_languages": [],
        "has_package_manager": False,
        "package_managers": [],

        # Testing
        "has_tests": False,
        "test_files_count": 0,

        # CI/CD
        "has_cicd": False,
        "cicd_platform": None,

        # Documentation
        "has_readme": False,
        "has_changelog": False,

        # Deployment
        "has_docker": False,
        "has_deployment_config": False,

        # Calculated
        "maturity_score": 0,
        "recommended_mode": "inception"
    }

    # Required SDLC documents
    required_sdlc = [
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

    # Check SDLC folder
    sdlc_path = path / "sdlc"
    if sdlc_path.exists() and sdlc_path.is_dir():
        findings["has_sdlc_folder"] = True
        existing_docs = [f.name for f in sdlc_path.glob("*.md")]
        findings["sdlc_docs"] = existing_docs
        findings["missing_sdlc_docs"] = [d for d in required_sdlc if d not in existing_docs]
    else:
        findings["missing_sdlc_docs"] = required_sdlc

    # Check Taskmaster
    taskmaster_path = path / ".taskmaster"
    if taskmaster_path.exists():
        findings["has_taskmaster"] = True
        tasks_file = taskmaster_path / "tasks" / "tasks.json"
        if tasks_file.exists():
            try:
                with open(tasks_file) as f:
                    tasks = json.load(f)
                    findings["taskmaster_task_count"] = len(tasks.get("tasks", []))
            except:
                pass

    # Check for code files
    code_extensions = {
        ".py": "Python",
        ".js": "JavaScript",
        ".ts": "TypeScript",
        ".jsx": "React",
        ".tsx": "React TypeScript",
        ".go": "Go",
        ".rs": "Rust",
        ".rb": "Ruby",
        ".java": "Java",
        ".cs": "C#",
        ".php": "PHP",
        ".swift": "Swift",
        ".kt": "Kotlin"
    }

    detected_langs = set()
    code_count = 0

    for ext, lang in code_extensions.items():
        files = list(path.rglob(f"*{ext}"))
        # Exclude node_modules, venv, etc.
        files = [f for f in files if "node_modules" not in str(f)
                 and "venv" not in str(f)
                 and ".venv" not in str(f)
                 and "__pycache__" not in str(f)]
        if files:
            detected_langs.add(lang)
            code_count += len(files)

    findings["has_code"] = code_count > 0
    findings["code_files_count"] = code_count
    findings["detected_languages"] = list(detected_langs)

    # Check package managers
    package_files = {
        "package.json": "npm/Node.js",
        "requirements.txt": "pip/Python",
        "Pipfile": "pipenv/Python",
        "pyproject.toml": "poetry/Python",
        "Cargo.toml": "cargo/Rust",
        "go.mod": "go modules",
        "Gemfile": "bundler/Ruby",
        "pom.xml": "maven/Java",
        "build.gradle": "gradle/Java"
    }

    for pkg_file, pkg_manager in package_files.items():
        if (path / pkg_file).exists():
            findings["has_package_manager"] = True
            findings["package_managers"].append(pkg_manager)

    # Check for tests
    test_patterns = [
        "test_*.py", "*_test.py",
        "*.test.js", "*.spec.js",
        "*.test.ts", "*.spec.ts",
        "*_test.go",
        "*_test.rs"
    ]

    test_count = 0
    for pattern in test_patterns:
        files = list(path.rglob(pattern))
        files = [f for f in files if "node_modules" not in str(f)]
        test_count += len(files)

    # Also check for test directories
    test_dirs = ["tests", "test", "__tests__", "spec"]
    for test_dir in test_dirs:
        if (path / test_dir).exists():
            test_count += len(list((path / test_dir).rglob("*")))

    findings["has_tests"] = test_count > 0
    findings["test_files_count"] = test_count

    # Check CI/CD
    cicd_configs = {
        ".github/workflows": "GitHub Actions",
        ".gitlab-ci.yml": "GitLab CI",
        ".circleci": "CircleCI",
        "Jenkinsfile": "Jenkins",
        ".travis.yml": "Travis CI",
        "azure-pipelines.yml": "Azure Pipelines"
    }

    for config_path, platform in cicd_configs.items():
        if (path / config_path).exists():
            findings["has_cicd"] = True
            findings["cicd_platform"] = platform
            break

    # Check documentation
    findings["has_readme"] = (path / "README.md").exists() or (path / "readme.md").exists()
    findings["has_changelog"] = (path / "CHANGELOG.md").exists() or (path / "changelog.md").exists()

    # Check deployment
    findings["has_docker"] = (path / "Dockerfile").exists() or (path / "docker-compose.yml").exists()

    deployment_files = ["vercel.json", "netlify.toml", "fly.toml", "render.yaml", "heroku.yml"]
    for df in deployment_files:
        if (path / df).exists():
            findings["has_deployment_config"] = True
            break

    # Calculate maturity score (0-100)
    score = 0

    # SDLC documentation (max 25 points)
    if findings["has_sdlc_folder"]:
        score += 5
        doc_ratio = len(findings["sdlc_docs"]) / len(required_sdlc)
        score += int(doc_ratio * 20)

    # Task management (max 10 points)
    if findings["has_taskmaster"]:
        score += 5
        if findings["taskmaster_task_count"] > 0:
            score += 5

    # Code (max 15 points)
    if findings["has_code"]:
        score += 10
        if findings["has_package_manager"]:
            score += 5

    # Testing (max 20 points)
    if findings["has_tests"]:
        score += 15
        if findings["test_files_count"] > 10:
            score += 5

    # CI/CD (max 15 points)
    if findings["has_cicd"]:
        score += 15

    # Documentation (max 5 points)
    if findings["has_readme"]:
        score += 3
    if findings["has_changelog"]:
        score += 2

    # Deployment (max 10 points)
    if findings["has_docker"]:
        score += 5
    if findings["has_deployment_config"]:
        score += 5

    findings["maturity_score"] = min(score, 100)

    # Determine recommended mode
    if findings["maturity_score"] < 20:
        findings["recommended_mode"] = "inception"
    elif findings["maturity_score"] < 80:
        findings["recommended_mode"] = "acceleration"
    else:
        findings["recommended_mode"] = "hardening"

    return findings


def create_config(project_name: str, mode: str, path: str = ".") -> dict:
    """Create forge.config.json."""

    config = {
        "project_name": project_name,
        "mode": mode,
        "current_phase": 1,
        "phase_progress": {
            "discovery": "pending",
            "architecture": "pending",
            "planning": "pending",
            "development": "pending",
            "quality": "pending",
            "deployment": "pending",
            "observability": "pending",
            "maintenance": "pending"
        },
        "integrations": {
            "taskmaster": False,
            "compound_engineering": False,
            "ralph_wiggum": False
        },
        "quality_gates": {
            "test_coverage_threshold": 80,
            "require_security_scan": True,
            "require_review": True
        },
        "checkpoints": [],
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }

    config_path = Path(path) / "forge.config.json"
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)

    return config


def generate_report(findings: dict) -> str:
    """Generate human-readable report."""

    report = []
    report.append("=" * 60)
    report.append("FORGE PROJECT SCAN REPORT")
    report.append("=" * 60)
    report.append(f"\nProject: {findings['project_name']}")
    report.append(f"Path: {findings['project_path']}")
    report.append(f"Scan Time: {findings['scan_time']}")

    report.append(f"\n{'-' * 40}")
    report.append("MATURITY ASSESSMENT")
    report.append(f"{'-' * 40}")
    report.append(f"Score: {findings['maturity_score']}/100")
    report.append(f"Recommended Mode: {findings['recommended_mode'].upper()}")

    report.append(f"\n{'-' * 40}")
    report.append("SDLC DOCUMENTATION")
    report.append(f"{'-' * 40}")
    report.append(f"SDLC Folder: {'Yes' if findings['has_sdlc_folder'] else 'No'}")
    if findings['sdlc_docs']:
        report.append(f"Existing Docs: {', '.join(findings['sdlc_docs'])}")
    if findings['missing_sdlc_docs']:
        report.append(f"Missing Docs: {', '.join(findings['missing_sdlc_docs'])}")

    report.append(f"\n{'-' * 40}")
    report.append("CODE ANALYSIS")
    report.append(f"{'-' * 40}")
    report.append(f"Has Code: {'Yes' if findings['has_code'] else 'No'}")
    report.append(f"Code Files: {findings['code_files_count']}")
    if findings['detected_languages']:
        report.append(f"Languages: {', '.join(findings['detected_languages'])}")
    if findings['package_managers']:
        report.append(f"Package Managers: {', '.join(findings['package_managers'])}")

    report.append(f"\n{'-' * 40}")
    report.append("TESTING")
    report.append(f"{'-' * 40}")
    report.append(f"Has Tests: {'Yes' if findings['has_tests'] else 'No'}")
    report.append(f"Test Files: {findings['test_files_count']}")

    report.append(f"\n{'-' * 40}")
    report.append("CI/CD & DEPLOYMENT")
    report.append(f"{'-' * 40}")
    report.append(f"Has CI/CD: {'Yes' if findings['has_cicd'] else 'No'}")
    if findings['cicd_platform']:
        report.append(f"Platform: {findings['cicd_platform']}")
    report.append(f"Has Docker: {'Yes' if findings['has_docker'] else 'No'}")
    report.append(f"Has Deployment Config: {'Yes' if findings['has_deployment_config'] else 'No'}")

    report.append(f"\n{'-' * 40}")
    report.append("TASK MANAGEMENT")
    report.append(f"{'-' * 40}")
    report.append(f"Taskmaster: {'Yes' if findings['has_taskmaster'] else 'No'}")
    if findings['has_taskmaster']:
        report.append(f"Task Count: {findings['taskmaster_task_count']}")

    report.append("\n" + "=" * 60)

    return "\n".join(report)


if __name__ == "__main__":
    project_path = sys.argv[1] if len(sys.argv) > 1 else "."

    # Scan project
    findings = scan_project(project_path)

    # Generate and print report
    report = generate_report(findings)
    print(report)

    # Output JSON for programmatic use
    print("\n--- JSON OUTPUT ---")
    print(json.dumps(findings, indent=2))
