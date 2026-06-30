# Design Decisions

## Purpose

FutureCATLeaf was designed to demonstrate how a multi-agent AI system can support enterprise functional incident investigations. The design transforms unstructured incident emails into structured, evidence-based investigations through a workflow of specialized AI agents and human review. The goal is to improve the accuracy, consistency, and efficiency of root cause analysis while ensuring that critical decisions remain under human oversight.

## Design Principles

| Principle                      | Why                                               |
| ------------------------------ | ------------------------------------------------- |
| Evidence before conclusions    | Prevent unsupported reasoning                     |
| Explainable AI                 | Every conclusion should reference evidence        |
| Human-in-the-loop              | AI assists, humans approve                        |
| Separation of responsibilities | Each agent has a single responsibility            |
| Structured data exchange       | Agents communicate using a common Incident Object |

These principles guided every architectural decision in FutureCATLeaf and were applied consistently throughout the design and implementation.

## Major Architectural Decisions

| Decision                  | Reason                               | Alternative Considered      |
| ------------------------- | ------------------------------------ | --------------------------- |
| Multi-agent architecture  | Clear separation of responsibilities | Single monolithic agent     |
| Incident Object           | Standard interface between agents    | Passing free-form text      |
| Human Review              | Responsible AI governance            | Fully autonomous approval   |
| Markdown Investigation Reports| Easy to read and version             | PDF-only reports            |
| Mock enterprise resources | Safe demonstration environment       | Live enterprise integration |

## AI Safety Decisions

| Decision | Rationale |
|----------|-----------|
| **Evidence-based reasoning**          | Conclusions are derived only from available evidence to reduce unsupported reasoning.|
| **"Insufficient Evidence" response**  | When available evidence is inconclusive, the system reports insufficient evidence rather than making unsupported conclusions. |
| **Human-in-the-loop review**          | Investigation results require human review and approval before they are considered final. |
| **Mock enterprise data**              | Development and demonstrations use mock data to avoid exposing sensitive information or impacting production systems. |
| **No automated production actions**   | The system provides recommendations only and does not modify enterprise applications, databases, or configurations. |
| **Complete audit trail**              | Structured Incident Objects, evidence, reasoning, and review decisions are preserved to support traceability and accountability. |
| **Clear responsibility boundaries**   | The system assists functional consultants but does not replace human judgment or decision-making. |

## Technology Decisions

| Technology                                               | Why Used                                                           |
| -------------------------------------------------------- | ------------------------------------------------------------------ |
| **Google ADK**                                           | Framework for building and orchestrating the multi-agent workflow. |
| **Gemini 2.5 Flash** *(or the exact model you're using)* | Structured reasoning, tool use, and report generation.             |
| **Python 3.11** *(if that's your actual version)*        | Primary application language.                                      |
| **Markdown**                                             | Human-readable investigation reports and documentation.            |
| **StructuredIncident.py**                                | Enforced consistency across agents                                 |
| **Local text/JSON resources**                            | Lightweight enterprise knowledge simulation for demonstrations.    |


## Trade-offs

| Decision                 | Benefit                                                                 | Trade-off                                                                 |
|--------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Multi-agent architecture | Clear separation of responsibilities, easier maintenance, and better explainability. | More components to manage and additional orchestration complexity.        |
| Structured Incident Object | Consistent communication between agents and easier auditing.            | Requires a predefined schema that must evolve as new requirements emerge. |
| Evidence-first reasoning | Produces explainable and traceable recommendations.                     | May return "Insufficient Evidence" instead of always providing an answer. |
| Human review before approval | Improves reliability and supports responsible AI governance.           | Adds a manual step before the investigation is finalized.                 |
| Mock enterprise resources | Safe for development, demonstrations, and learning without exposing sensitive data. | Does not fully represent the complexity of real enterprise environments.  |
| Markdown report generation | Easy to read, version control, and share.                              | Less suitable for highly formatted business reports than PDF or Word documents. |
| Local file-based knowledge | Simple to develop and demonstrate without external dependencies.        | Limited scalability compared to enterprise knowledge bases or RAG systems. |

These trade-offs were intentional. The primary objective of FutureCATLeaf was to demonstrate a reliable, explainable, and responsible AI-assisted investigation workflow suitable for learning and proof-of-concept purposes. Where trade-offs existed, the design consistently favored transparency, maintainability, and human oversight over automation and complexity.

## Lessons Learned
- Domain knowledge significantly improves AI output quality.
- Structured intermediate objects simplify multi-agent workflows.
- Human review remains essential for enterprise support scenarios.
- Good documentation is as important as good code.
- AI systems benefit from iterative refinement using user feedback.

## Future Improvements

FutureCATLeaf has been designed with extensibility in mind. The following enhancements are planned for future versions:

| Enhancement | Benefit |
|-------------|---------|
| ServiceNow integration | Automatically retrieve and update incident details from enterprise ticketing systems. |
| Oracle Database integration | Query live master data, configuration tables, and transactional information during investigations. |
| Email integration | Automatically ingest incident emails from enterprise mailboxes. |
| Semantic search (RAG) | Search Functional Reference Guides, user manuals, and historical RCA documents using natural language. |
| Web-based dashboard | Provide a graphical interface for investigation, review, and report management. |
| Learning from approved investigations | Build a knowledge repository of approved RCAs to assist future investigations. |
| Additional investigation agents | Introduce specialized agents for areas such as database validation, deployment analysis, and business rule verification. |
| Analytics and reporting | Identify recurring incidents, root cause trends, and support performance metrics. |
| Multi-user collaboration | Enable multiple reviewers, comments, approval workflows, and investigation history. |
| Enterprise authentication | Integrate with enterprise identity providers to support secure user authentication and role-based access. |

## Closing Remarks

FutureCATLeaf demonstrates how Generative AI can support enterprise functional consultants through an evidence-based, explainable, and human-governed investigation workflow. The current implementation serves as a proof of concept, while the architecture provides a strong foundation for future enterprise integrations and enhancements.