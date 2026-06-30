# FutureCATLeaf Capstone Demo Script

# FutureCATLeaf – AI-Assisted Functional Investigation System

**Tagline:**
*Evidence First. Reason Second. Human Always.*

---

# Demo Duration

Approximately **5 minutes**

---

# 1. Introduction (30 seconds)

Hello everyone.

This project is called **FutureCATLeaf**, an AI-assisted functional investigation system designed for enterprise application support teams.

When a business incident is reported through email, functional analysts typically spend significant time gathering evidence from multiple systems before identifying the likely root cause.

FutureCATLeaf demonstrates how a multi-agent AI system can assist analysts by collecting evidence, reasoning transparently, involving a human reviewer, and producing a structured Functional Investigation Report.

The project is implemented using **Google ADK**, **Gemini**, and local mock enterprise resources.

---

# 2. Problem Statement (45 seconds)

Traditional incident investigation has several challenges:

* Incident information is often unstructured.
* Evidence is scattered across multiple systems.
* AI assistants may generate conclusions without sufficient evidence.
* Investigation documentation is often created manually.
* Enterprise decisions require human validation.

FutureCATLeaf addresses these challenges through an evidence-first, human-in-the-loop approach.

---

# 3. Solution Architecture (60 seconds)

The solution consists of five specialized AI agents.

1. **Email Processing Agent**

   * Reads the incident email.
   * Converts unstructured text into a Structured Incident Object.

2. **Investigation Agent**

   * Searches mock enterprise resources.
   * Collects logs, deployment history, master data, and knowledge documents.

3. **Evidence-Based Root Cause Agent**

   * Generates multiple hypotheses.
   * Evaluates supporting and contradicting evidence.
   * Identifies the most probable root cause or reports insufficient evidence.

4. **Human Review Agent**

   * Presents the investigation summary.
   * Captures reviewer approval or revision comments.

5. **Report Generator**

   * Produces a Markdown Functional Investigation Report.
   * Produces a JSON audit object for traceability.

---

# 4. Live Demonstration (90 seconds)

Run the application.

```bash
python main.py
```

During execution demonstrate:

* Incident email is processed.
* Structured Incident Object is created.
* Investigation Agent searches enterprise resources.
* Evidence is collected.
* Root Cause Agent performs evidence-based reasoning.
* Human reviewer approves the investigation.
* Markdown report is generated.
* JSON audit object is generated.

Show the generated files inside the **reports/** directory.

---

# 5. Responsible AI (45 seconds)

Responsible AI was an important design goal throughout this project.

FutureCATLeaf incorporates several safeguards:

* Evidence before conclusions
* Explainable reasoning
* Human approval before finalization
* Mock enterprise data only
* No automated enterprise actions
* Complete audit trail
* Explicit handling of insufficient evidence

These safeguards help reduce hallucinations while increasing transparency and trust.

---

# 6. Project Highlights (30 seconds)

Key capabilities include:

* Multi-agent architecture
* Structured Incident Object
* Evidence-based reasoning
* Explainable AI
* Human-in-the-loop workflow
* Automated investigation report generation
* JSON audit output

---

# 7. Future Roadmap (30 seconds)

Potential future enhancements include:
FutureCATLeaf is designed as a foundation that can be extended for real enterprise environments. Planned enhancements include:

- ServiceNow integration
- Oracle Database integration
- Gmail incident ingestion
- Semantic search over Functional Reference Guides
- Learning from approved investigations
- Interactive web dashboard
- Analytics and incident trend reporting
- Multi-user workflow

---

# 8. Closing (20 seconds)

FutureCATLeaf demonstrates how AI can assist enterprise functional analysts by improving investigation efficiency while ensuring transparency, accountability, and human oversight.

The guiding principle of the project is:

> **Evidence First. Reason Second. Human Always.**

Thank you.
