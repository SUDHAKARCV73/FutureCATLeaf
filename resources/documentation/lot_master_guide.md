# Lot Master Guide

## Overview

The **Grade Master** is a master data configuration created at the beginning of each processing season. It defines all available grades and their associated lot numbers used during processing and label printing.

---

# 1. Grade Master

The Grade Master maintains the details of each grade.

## Information Maintained

| Field                 | Description                                  |
| --------------------- | -------------------------------------------- |
| **Grade Code**        | Unique code identifying the grade            |
| **Grade Description** | Description of the grade                     |
| **Product Type**      | Product category (e.g., Lamina, Stem, Fines) |
| **Grade Price**       | Standard price associated with the grade     |

---

# 2. Lot Details

Each grade can have one or more lot numbers associated with it.

The following information is maintained for every lot.

| Field          | Description                                     |
| -------------- | ----------------------------------------------- |
| **Lot Number** | Unique lot identifier                           |
| **Label Type** | Label format to be used while printing          |
| **Status**     | Indicates whether the lot is Active or Inactive |

---

# 3. Business Rules

The following business rules shall be enforced by the system:

### Rule 1 – Active Lot

* A grade may contain multiple lot numbers.
* **Only one lot number can be Active at any point in time.**
* Activating a new lot should automatically deactivate the previously active lot, or the system should prevent multiple active lots.

### Rule 2 – Label Type

* Every active lot must have a valid **Label Type** assigned.
* The Label Type determines which label format will be used during label printing.

---

# 4. Common Configuration Issues

The following configuration issues may result in incorrect or failed label printing.

## 4.1 Label Type Not Defined

**Issue**

The **Label Type** is left blank (NULL).

**Impact**

* The system cannot determine which label format to print.
* Label printing may fail or an incorrect label may be generated.

**Recommendation**

Always assign a valid Label Type before activating a lot number.

---

## 4.2 Multiple Active Lot Numbers

**Issue**

More than one lot number is marked as **Active** for the same grade.

**Impact**

* The system cannot uniquely determine which lot number should be used.
* This may lead to incorrect labels being printed or inconsistent processing.

**Recommendation**

Ensure that **only one Active lot number exists per grade**.

---

# 5. Validation Recommendations

The system should perform the following validations during save or update:

| Validation                                  | Expected Result                                                                           |
| ------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Label Type is blank                         | Display validation error and prevent saving.                                              |
| More than one Active lot exists for a grade | Display validation error and prevent saving.                                              |
| No Active lot exists for a grade            | Display validation error and prevent saving if the grade is intended for operational use. |

---

# Process Flow

```text
Create Grade
      │
      ▼
Add Lot Numbers
      │
      ▼
Assign Label Type
      │
      ▼
Activate One Lot Number
      │
      ▼
System Validations
      │
      ├── Exactly One Active Lot
      ├── Label Type Defined
      ▼
Ready for Label Printing
```

	
