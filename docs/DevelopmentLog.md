# Development Log - FutureCATLeaf

## [2026-06-27] V1 Email Processing Agent Implementation

### Objectives
- Implement the Email Processing Agent to parse functional support incident emails.
- Transition incoming email text to a structured JSON incident object.

### Implementation Details
- Created mock email file at `data/incidents/incident_lot_number.txt`.
- Created prompt instructions at `prompts/email_processor.md` enforcing strict JSON extraction schemas and specific hardcoded default values.
- Created `tools/file_tools.py` containing the custom tool `read_incident_email` for the agent.
- Created `agents/email_processor.py` utilizing the Google ADK to instantiate an `Agent` with the system instructions and custom tool.
- Created `main.py` configuring the `Runner` and executing the agent on the mock email file.

### Refinements & Validation
- Improved prompt instructions in `prompts/email_processor.md` to set `module` to `"Packed Output"` when `impacted_screen` contains `"Packed Output screen"`.
- Improved default/missing information rule to identify missing support data: `"Error logs, active lot number status, recent deployment details"`.
- Verified warning-free clean JSON execution in terminal output.

## [2026-06-27] V2 Enhancements: Dynamic Ingestion, Extra Fields, and Confidence Ratings

### Objectives
- Support processing any incident file path provided as a command-line parameter.
- Print helpful usage instructions if no path is provided.
- Add five new schema fields: `business_impact`, `reported_by`, `reported_date`, `confidence` (string value: `"High"`, `"Medium"`, or `"Low"`), and `attachments`.
- Enforce robustness across writing styles and spelling variants.

### Implementation Details
- Updated [main.py](file:///d:/AllProjects/FutureCATLeaf/main.py) to check for input arguments. If `len(sys.argv) < 2`, it shows a usage help message and exits.
- Resolves absolute/relative paths and handles errors if the file doesn't exist.
- Enhanced [email_processor.md](file:///d:/AllProjects/FutureCATLeaf/prompts/email_processor.md) to define the new fields. Configured `confidence` to be a single string. If key fields (e.g. `module`, `process`, `priority`) are inferred, confidence is downgraded to `"Medium"` or `"Low"`.
- Added output cleaning to [main.py](file:///d:/AllProjects/FutureCATLeaf/main.py) to ensure clean JSON stdout without code block wrappers.

## [2026-06-27] V2 Refinement: Business Impact Inference

### Objectives
- Automatically infer concise business impact statements when a user reports being unable to complete key processes (e.g., plan finalization, print label, sync mobile, etc.).
- Ensure overall extraction confidence is restricted to `"Medium"` or `"Low"` if the business impact is inferred.

### Implementation Details
- Updated extraction instructions in [email_processor.md](file:///d:/AllProjects/FutureCATLeaf/prompts/email_processor.md) to parse process failures and infer business impact (e.g., `"Unable to make plan final" -> "Processing plan cannot be finalized, which may block downstream processing activities."`).
- Verified execution on `Incident_unable_to_make_plan_final.txt`. It correctly returned the inferred business impact string and downgraded overall confidence to `"Medium"`.

## [2026-06-27] Phase 2: Investigation Agent Implementation

### Objectives
- Build an Investigation Agent to collect facts and evidence from local mock resources.
- Do not conclude root cause, draft RCAs, or make decisions—gather evidence in a neutral manner.
- Keep `rca`, `investigation`, and `approval` fields as `null`.

### Implementation Details
- Created mock files in `resources/` covering logs, deployments, master data (lot master, shift calendar), and past RCAs.
- Implemented custom search tools in [resource_tools.py](file:///d:/AllProjects/FutureCATLeaf/tools/resource_tools.py) to read and filter these files.
- Configured the Investigation Agent in [investigation_agent.py](file:///d:/AllProjects/FutureCATLeaf/agents/investigation_agent.py) with prompts in [investigation_agent.md](file:///d:/AllProjects/FutureCATLeaf/prompts/investigation_agent.md).
- Updated [main.py](file:///d:/AllProjects/FutureCATLeaf/main.py) to sequentially run the **Email Processor Agent**, parse its output, run the **Investigation Agent with the output, and print the final JSON.
- Verified evidence retrieval on both plan finalization and lot printing incidents.

## [2026-06-27] Phase 2 Refinement: Evidence Schema Extension & Fallback Filtering

### Objectives
- Extend the evidence object schema to include `"resource"` (the filename searched) and `"reason"` (relevance justification).
- Do not add the fallback evidence item if at least one matching evidence item has already been successfully identified.
- Ensure the agent remains strictly neutral, explaining *only* the facts and their relevance, and never stating a Root Cause, Fix, or Recommendation.

### Implementation Details
- Modified [investigation_agent.md](file:///d:/AllProjects/FutureCATLeaf/prompts/investigation_agent.md) to include the updated schema layout, strict neutrality guidelines, and conditional fallback instruction.
- Verified output schemas on both plan finalization and lot number printing mock incidents.

## [2026-06-28] Phase 3: Evidence-Based Root Cause Reasoning Agent Implementation

### Objectives
- Build an RCA Agent (Root Cause Analysis Agent) to evaluate gathered evidence and populate a structured `rca` object.
- Integrate the agent into a 3-agent sequential pipeline: `Email Processor Agent` ➔ `Investigation Agent` ➔ `RCA Agent`.
- Follow strict safety guidelines: no database SQL modifications, safe validation actions, and keep `approval` as `null`.

### Implementation Details
- Created [rca_agent.md](file:///d:/AllProjects/FutureCATLeaf/prompts/rca_agent.md) defining the detailed structured schema for the `rca` field, including hypothesis matrices and confidence scores.
- Created [rca_agent.py](file:///d:/AllProjects/FutureCATLeaf/agents/rca_agent.py) configuring the ADK Agent.
- Modified [main.py](file:///d:/AllProjects/FutureCATLeaf/main.py) to chain all three agents in order, passing clean JSON outputs between them and suppressing user warnings.
- Verified the final output on `Incident_unable_to_make_plan_final.txt`. It correctly retains all 21 schema fields and populates the structured `rca` object.

## [2026-06-28] Phase 3 Refinement: Validation Steps List Formatting

### Objectives
- Modify the `recommended_validation_steps` schema from a single string to an array of strings representing a list of validation steps.

### Implementation Details
- Updated prompt instructions in [rca_agent.md](file:///d:/AllProjects/FutureCATLeaf/prompts/rca_agent.md) to define `recommended_validation_steps` as an `(array of strings)`.
- Verified formatting output in batch check runs. It correctly formatted validation steps as an array.

## [2026-06-28] Phase 4: Human Review Agent Implementation

### Objectives
- Build a Human Review Agent to update the `approval` object inside the Incident Object based on reviewer input.
- Keep implementation simple and provide interactive terminal workflows for approval decisions.

### Implementation Details
- Created [review_agent.md](file:///d:/AllProjects/FutureCATLeaf/prompts/review_agent.md) outlining instructions for the Review Agent to update status, reviewer name, comments, and date inside the `approval` object.
- Created [review_agent.py](file:///d:/AllProjects/FutureCATLeaf/agents/review_agent.py) configuring the ADK Agent.
- Modified [main.py](file:///d:/AllProjects/FutureCATLeaf/main.py) to print the report summary to the terminal, prompt for reviewer name, Y/N approval, and review comments, then invoke the Review Agent.
- Verified terminal output and final JSON object formatting.

## [2026-06-28] Phase 5: Functional Investigation Report Generator Implementation

### Objectives
- Build a Functional Investigation Report Generator Agent to format the finalized Incident Object into a Markdown report.
- Save both the Markdown report and the final JSON object in the `reports/` folder.

### Implementation Details
- Created [report_generator.md](file:///d:/AllProjects/FutureCATLeaf/prompts/report_generator.md) for Markdown formatting.
- Created [report_generator.py](file:///d:/AllProjects/FutureCATLeaf/agents/report_generator.py) configuring the ADK Agent.
- Modified [main.py](file:///d:/AllProjects/FutureCATLeaf/main.py) to execute the report generator, save files, and print paths.

## [2026-06-28] V5 Refinements: Documentation Integration & Bale Issue Resolution

### Objectives
- Search functional reference documentation under `resources/documentation/` before inspecting deployments.
- If a functional guide contains rules for the process, include it as evidence under the `"Functional Reference Guide"` source.
- Avoid preferring deployments unless logs/master data support it.
- Resolve bale issues by prioritizing status validations (e.g. status 'S' Stocked vs. Quarantined) over RFID scanner defect hypotheses unless RFID is explicitly mentioned.
- Do not automatically regenerate RCA if review comments contradict the report, keeping them visible in the generated document.

### Implementation Details
- Added `search_functional_documentation` to [resource_tools.py](file:///d:/AllProjects/FutureCATLeaf/tools/resource_tools.py) to read matching `.md` files.
- Bound the tool to the Investigation Agent in [investigation_agent.py](file:///d:/AllProjects/FutureCATLeaf/agents/investigation_agent.py).
- Enhanced prompt keywords and ordering constraints in [investigation_agent.md](file:///d:/AllProjects/FutureCATLeaf/prompts/investigation_agent.md) to search logs using simple atomic queries.
- Added preference and governance rules to [rca_agent.md](file:///d:/AllProjects/FutureCATLeaf/prompts/rca_agent.md).
- Verified the complete sequential pipeline on the bale issue `incident_unble_issue_bales_processing.txt`, yielding correct status quarantined diagnosis and Functional Reference Guide evidence.
