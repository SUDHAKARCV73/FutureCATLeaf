# Historical RCA Records - FutureCATLeaf Knowledge Base

## RCA-00249: Shift Schedule Generation Gap (Oracle Shift Validation Error)
- **Incident Summary**: Users in South Africa reported ORA-20001: No shifts defined for processing week.
- **Root Cause**: The shift scheduler job was not run for the holiday week, leaving the shift table empty (draft status) for the requested market and dates.
- **Remediation**: Populate shift records for the week and update status to 'APPROVED' in shift master tables.

## RCA-00183: Reprinting Label Gradients Cache Issue
- **Incident Summary**: Reprinting packed case label displayed old grade.
- **Root Cause**: Reprinting processes retrieved case records from temporary cache before database commit finished regrading write operations.
- **Remediation**: Clear cache and wait for committed database updates before starting reprinting.
