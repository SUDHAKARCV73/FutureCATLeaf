1. processing_plan_guide.md

   - What is processing plan: This is plan for generation of boxes or packed cases for each product type. The Blend details, green leaf % mix. Plan Test on the operation.

## 1.2 Processing Plan Information

The following information shall be available:

| Field            | Description             |
| ---------------- | ----------------------- |
| Plan Number      | Unique plan number      |
| Week Number      | Processing week         |
| Demand Reference | Linked demand           |
| Planned Quantity | Quantity to process     |
| Blend Plan       | Blend requirements      |
| Testing Plan     | Testing requirements    |
| Status           | Tentative, Final, Ready |

Most information shall be automatically derived from Demand Planning.


# 2. Processing Plan Status Management

## 2.1 Tentative Status

### Purpose

Initial planning stage.

### Functional Rules

Users may:

* Modify quantities
* Modify blend plans
* Modify testing plans
* Modify planning details

No operational activities can begin.

---

## 2.2 Final Status

### Purpose
   
Planning review completed. There should be space in week to perform the operation. Meaning in a week if 3 plans have already finalized and we have just 4 hours left after the accommodation of 3 plans. Based the line capacity(2000kg per hour)you can process max of 8000Kg for 4th plan. If the plan is beyond that the plan cannot be made final. If there is no weekly shift plan defined for the week then plan cannot be made final. 

### Functional Rules

System shall:

* Prevent modification of plan data.
* Allow status reversal back to Tentative if operations have not started.

Users may:

Final → Tentative

for further modifications.

---

## 6.3 Ready Status

### Purpose

Operational execution approved.

### Functional Rules

Status becomes Ready after Issue Instructions are generated.

Once Ready:

* Plan becomes operational.
* Reversion to final to Tentative is not allowed.
* Modifications shall not be permitted.

- Shift calendar dependency: Called weekly shift plan in FCL. If there is no weekly shift plan defined for the week then plan cannot be made final. Weekly shift plan contains 2 shifts or 3 shifts per day defined according to market. This is a pre-requisite to creating processing plan.
 
- Common errors
Trying to create processing plan without weekly shift plan or demand. 
All plans should be closed/ cancelled to move to the next week.
Having enough remaining time for processing.
Blend plan would be accepted only if sufficient stock is available and plan cannot be finalized,