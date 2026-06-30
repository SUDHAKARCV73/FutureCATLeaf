# Green Leaf Processing

## Overview

Green Leaf Processing is the process of issuing green leaf to the processing line for production. It is also referred to as **Feeding**.

This process can be performed only after:

* The **Processing Plan** has been converted into an operational plan.
* The corresponding **Feed Shift** has been opened.

The Green Leaf Processing screen contains multiple tabs. The primary tabs are:

* Green Bale Issue
* Pallet Issue
* Refeeds

---

# 1. Green Bale Issue

The **Green Bale Issue** tab is used to issue individual green bales to the processing line.

Each bale is identified by scanning or entering its unique bale number.

## Business Rules

The system allows a bale to be issued only when:

* The bale exists in the system.
* The bale status is **'S' (Stocked)**.
* The bale has not already been issued.
* The bale grade is included in the planned blend defined in the Processing Plan.

If any of these conditions are not met, the system prevents the bale from being issued and displays an appropriate validation message.

---

# 2. Pallet Issue

A **Pallet** (also referred to as a **Rack**) is used to store multiple green bales together.

Instead of scanning every individual bale, the operator can scan a single pallet.

The system automatically identifies all bales stored on that pallet and issues them to the processing line.

## Advantages

* Faster processing
* Reduced scanning effort
* Lower possibility of manual scanning errors
* Improved operational efficiency

## Business Rules

Before issuing a pallet, the system validates that:

* The pallet exists.
* All bales on the pallet are available for issue.
* Every bale has a status of **'S' (Stocked)**.
* Every bale belongs to a grade included in the planned blend.

If any bale on the pallet fails validation, the pallet issue transaction is rejected.

---

# 3. Refeeds

The **Refeeds** tab is used to return previously packed material back into the processing line.

This process is generally performed when packed cases are rejected during quality inspection and require reprocessing.

## Typical Reasons for Refeed

* Quality rejection
* Product does not meet specification
* Reprocessing required

The system records the quantity being re-fed so that inventory and production records remain accurate.

---

# 4. Validations

The system performs the following validations before allowing an issue transaction.

| Validation                              | Expected Result      |
| --------------------------------------- | -------------------- |
| Processing Plan is operational          | Processing allowed   |
| Feed Shift is open                      | Processing allowed   |
| Bale exists                             | Processing allowed   |
| Bale Status = 'S' (Stocked)             | Processing allowed   |
| Bale already issued                     | Transaction rejected |
| Bale grade exists in planned blend      | Processing allowed   |
| Pallet exists                           | Processing allowed   |
| All bales on pallet satisfy validations | Pallet issue allowed |

---

# 5. Common Error Conditions

| Error Condition                 | Possible Cause                              |
| ------------------------------- | ------------------------------------------- |
| Bale not found                  | Invalid bale number scanned                 |
| Bale is not in Stock            | Bale status is not **'S'**                  |
| Bale already issued             | Bale has already been fed to production     |
| Grade not planned               | Bale grade is not part of the planned blend |
| Pallet not found                | Invalid pallet scanned                      |
| Feed Shift not open             | Processing shift has not been opened        |
| Processing Plan not operational | Plan has not been released for execution    |

---

# Process Flow

```text
Processing Plan Finalized
          │
          ▼
Convert to Operational Plan
          │
          ▼
Open Feed Shift
          │
          ▼
Select Issue Method
     ┌───────────────┐
     │               │
     ▼               ▼
Green Bale Issue   Pallet Issue
     │               │
     └───────┬───────┘
             ▼
System Validations
             │
             ▼
Issue to Processing Line
             │
             ▼
Update Inventory
             │
             ▼
Refeed (if Quality Rejects Packed Cases)
```
