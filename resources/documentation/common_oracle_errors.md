# Common Oracle Errors – Functional Troubleshooting Guide

## Overview

This document provides a quick reference for commonly encountered Oracle database errors, their possible functional meaning, and where to investigate the issue before escalating it to the technical team.

---

# 1. Where to Check the Error

## Oracle Forms

When an Oracle error is displayed in Oracle Forms:

1. Note the error message.
2. Navigate to:

```
Help → Display Errors
```

3. Review the complete Oracle error stack.
4. Capture the error message and share it with the support team if required.

---

## Mobile Application

When an error occurs during synchronization:

Check the following:

* Mobile Sync Status
* Synchronization Log
* API Response (if available)
* Server/Application Logs
* Oracle Error returned during synchronization

Record the complete Oracle error message before proceeding with analysis.

---

# 2. Common Oracle Errors

| Oracle Error                                                         | Possible Functional Meaning                                        | Recommended Functional Checks                                            |
| -------------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| **ORA-00001** Unique Constraint Violated                             | Duplicate record already exists.                                   | Verify whether the same transaction or master record already exists.     |
| **ORA-01400** Cannot Insert NULL                                     | Mandatory information is missing.                                  | Check whether all mandatory fields have been entered.                    |
| **ORA-01403** No Data Found                                          | Required master or transaction data is missing.                    | Verify that the expected record exists in the application.               |
| **ORA-01422** Exact Fetch Returns More Than Requested Number of Rows | Duplicate master data exists where only one record is expected.    | Check for duplicate configuration or master records.                     |
| **ORA-01722** Invalid Number                                         | A numeric field contains invalid data.                             | Verify numeric fields and imported data values.                          |
| **ORA-01843** Not a Valid Month                                      | Invalid date format.                                               | Check the entered date and application date format.                      |
| **ORA-01861** Literal Does Not Match Format String                   | Date format mismatch.                                              | Verify the expected date format and user input.                          |
| **ORA-02290** Check Constraint Violated                              | Business validation failed.                                        | Review business rules and entered values.                                |
| **ORA-02291** Parent Key Not Found                                   | Referenced master record does not exist.                           | Ensure the related master record has been created.                       |
| **ORA-02292** Child Record Found                                     | Record cannot be deleted because dependent records exist.          | Check related transactions before attempting deletion.                   |
| **ORA-04068** Existing Package State Discarded                       | Package has been recompiled during execution.                      | Retry the transaction. If the issue persists, contact technical support. |
| **ORA-04088** Error During Trigger Execution                         | Business logic inside a trigger failed.                            | Review the business transaction that triggered the error.                |
| **ORA-06502** Numeric or Value Error                                 | Invalid data length, number conversion, or variable size exceeded. | Verify field lengths and entered values.                                 |
| **ORA-06512** PL/SQL Stack Trace                                     | Indicates where the actual error occurred.                         | Review accompanying Oracle errors to identify the root cause.            |
| **ORA-08177** Cannot Serialize Access                                | Record is being updated by another user.                           | Retry the transaction after a short interval.                            |
| **ORA-12154** TNS Could Not Resolve Connect Identifier               | Database connection configuration issue.                           | Verify database connectivity and TNS configuration.                      |
| **ORA-12514** Listener Does Not Currently Know of Service            | Database service is unavailable.                                   | Verify listener status and database availability.                        |
| **ORA-12541** No Listener                                            | Database listener is not running.                                  | Verify that the database listener service is running.                    |
| **ORA-28000** Account Locked                                         | Database account has been locked.                                  | Contact the Database Administrator (DBA).                                |

---

# 3. Functional Troubleshooting Checklist

Before raising an incident, verify the following:

* Master data is available.
* Mandatory fields have been entered.
* The transaction has not already been created.
* The selected grade, item, customer, or location exists.
* Required configuration is active.
* The processing date falls within the valid period.
* The user has the required access rights.
* Network connectivity is available (for mobile synchronization).

---

# 4. Information to Capture Before Escalation

Include the following information when reporting an issue:

* Oracle Error Number (for example, **ORA-01403**)
* Complete error message
* Screen or process name
* User ID
* Date and time of occurrence
* Steps performed before the error
* Screenshot of the error (if available)
* Whether the issue occurred in:

  * Oracle Forms
  * Mobile Application
  * Mobile Synchronization

---

# 5. Escalation Guidelines

Escalate the issue to the technical team when:

* The Oracle error persists after functional validation.
* The issue is reproducible.
* The error originates from a PL/SQL package, trigger, or database object.
* Database connectivity errors are encountered.
* Multiple users experience the same issue.

---

# Quick Decision Flow

```text
Oracle Error Occurs
        │
        ▼
Is it Oracle Forms?
        │
   ┌────┴────┐
   │         │
  Yes       No
   │         │
Help →      Check Mobile
Display     Sync Logs
Errors      and API Response
   │         │
   └────┬────┘
        ▼
Identify ORA Error
        │
        ▼
Perform Functional Checks
        │
        ▼
Issue Resolved?
    │
 ┌──┴──┐
 │     │
Yes    No
 │      │
Done    Escalate to Technical Team
```
