# Weekly Shift Plan – Prerequisites for Processing Plan

The **Weekly Shift Plan** is a prerequisite for creating the **Processing Plan**. It defines the operational shifts for each week and ensures that planning is performed only within the configured working schedule.

---

# 1. Shift Master

The **Shift Master** maintains the list of available shifts that can be scheduled during planning.

## Information Maintained

| Field           | Description                                       |
| --------------- | ------------------------------------------------- |
| **Shift Code**  | Unique identifier of the shift                    |
| **Description** | Name or description of the shift                  |
| **Start Time**  | Shift start time                                  |
| **End Time**    | Shift end time                                    |
| **Status**      | Indicates whether the shift is Active or Inactive |

---

# 2. Processing Season

The **Processing Season** defines the operational period during which processing activities are carried out.

## Information Maintained

* Processing Season Start Date
* Processing Season End Date

After the Processing Season is created, the system generates the corresponding week details.

---

# 3. Week Details

The **Week Details** table stores the calendar weeks that belong to the Processing Season.

## Information Maintained

| Field           | Description            |
| --------------- | ---------------------- |
| **Week Number** | Sequential week number |
| **Start Date**  | First day of the week  |
| **End Date**    | Last day of the week   |

These weeks are used while defining the Weekly Shift Plan.

---

# 4. Weekly Shift Plan

The **Weekly Shift Plan** associates working shifts with each week.

Shift information is maintained **day-wise** for every week.

## Information Maintained

| Field                      | Description                      |
| -------------------------- | -------------------------------- |
| **Date**                   | Working date                     |
| **Shift Code**             | Shift assigned for the day       |
| **Team Lead**              | Person responsible for the shift |
| **Number of Team Members** | Planned workforce for the shift  |

The Weekly Shift Plan represents the operational capacity available for scheduling.

---

# 5. Validation Rules

The following validations shall be performed before a Processing Plan is finalized:

* A Weekly Shift Plan must exist for the selected week.
* Processing can only be scheduled within the dates defined in the Weekly Shift Plan.
* Processing cannot be scheduled for dates where no shift has been configured.

If any of the above validations fail, the Processing Plan shall not be finalized.

---

# 6. Error Handling

## Error Message

```text
No shifts available.
```

### Error Conditions

The above message is displayed when:

* No Weekly Shift Plan exists for the selected week.
* Processing is scheduled beyond the configured planning period.
* No shift has been defined for the selected date.

---

# Process Flow

```text
Processing Season
        │
        ▼
Generate Week Details
        │
        ▼
Create Weekly Shift Plan
(Date → Shift → Team Lead → Team Members)
        │
        ▼
Create Processing Plan
        │
        ▼
System Validation
        │
        ├── Weekly Shift Plan Exists
        │          │
        │          ▼
        │   Processing Allowed
        │
        └── Weekly Shift Plan Missing
                   │
                   ▼
        Display Error:
        "No shifts available."
```

This version is suitable for inclusion in a **Functional Specification (FS)** or **Solution Design Document (SDD)** and avoids any domain-specific references. 
