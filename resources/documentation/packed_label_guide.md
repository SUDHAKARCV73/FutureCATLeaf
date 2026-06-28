## 1 Packed Case Output

### 1.1 Purpose

Capture finished packed product information. There are 3 product types that comes out of processing Lamina, Stem and fines. These products are packed according to customer requirements.

Examples:

* 200 Kg Cartons
* String Packs
* Other defined packing styles

---

## 1.2 Label Generation

For every packed case, the system shall generate a unique label. The label definition is provided in the packed grade master. For each lot number a label is associated. At any point of time there is only one active lot number for a grade. It is not mandatory to have a lot number active. If there is no lot number active then no label gets printed. So when a case is generated, the same screen have a print lable button once you click on the button the label for the active lot number is generated. 

### Label Information

| Field        | Description             |
| ------------ | ----------------------- |
| Case Number  | Unique case identifier  |
| Packed Grade | Product grade           |
| Lot Number   | Production lot          |
| Net Weight   | Product weight          |
| Gross Weight | Total weight            |
| Tare Weight  | Packing material weight |
| Barcode      | Encoded case number     |

The barcode shall uniquely identify the packed case for traceability purposes.
