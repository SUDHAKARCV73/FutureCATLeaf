# Changelog

All notable changes to this project will be documented in this file.

The project follows [Semantic Versioning](https://semver.org/).

---

## [1.0.0] - Initial MVP Release

### Added

#### Email Processing Agent

* Reads mock incident emails.
* Converts unstructured incident text into a Structured Incident Object.
* Extracts key business information for downstream processing.

#### Investigation Agent

* Searches local mock enterprise resources.
* Collects evidence from logs, deployment history, master data, and knowledge documents.
* Builds an evidence package for analysis.

#### Evidence-Based Root Cause Reasoning Agent

* Evaluates multiple root cause hypotheses.
* Identifies supporting and contradicting evidence.
* Detects unresolved evidence gaps.
* Determines the most probable root cause.
* Recommends validation steps, workaround, corrective action, and preventive action.
* Reports "Insufficient Evidence" when a reliable conclusion cannot be reached.

#### Human Review Agent

* Presents the investigation summary.
* Captures reviewer name.
* Supports approval or rejection of AI findings.
* Records reviewer comments for audit purposes.

#### Functional Investigation Report Generator

* Generates a Markdown Functional Investigation Report.
* Generates a JSON audit object containing the investigation details and review outcome.

### Responsible AI

* Evidence-first investigation workflow.
* Explainable reasoning with supporting evidence.
* Human-in-the-loop approval before report finalization.
* Mock enterprise resources only.
* No automated enterprise actions.
* Complete investigation audit trail.
* Transparent handling of insufficient evidence.

### Project Features

* Multi-agent architecture using Google ADK and Gemini.
* Structured Incident Object shared across all agents.
* Modular and extensible workflow design.
* Local mock enterprise resource repository.
* Markdown and JSON output generation.
* Enterprise-oriented functional investigation workflow.
