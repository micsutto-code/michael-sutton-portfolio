# Filter: By Area Code

## Description
Displays only customers matching a target area code.

## Pseudocode
```
START

INPUT targetAreaCode
INPUT areaCode

WHILE areaCode != 999

    INPUT phoneNumber
    INPUT messages

    CALL ComputeBill(messages) → totalBill

    IF areaCode == targetAreaCode THEN
        DISPLAY areaCode, phoneNumber, totalBill
    END IF

    INPUT areaCode

END WHILE

END
```
