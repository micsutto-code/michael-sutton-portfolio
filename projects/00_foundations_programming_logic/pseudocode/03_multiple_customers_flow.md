# Multiple Customers Flow

## Description
Processes multiple customers using a sentinel value.

## Pseudocode

START

INPUT areaCode

WHILE areaCode != 999

    INPUT phoneNumber
    INPUT messages

    CALL ComputeBill(messages) → totalBill

    DISPLAY areaCode, phoneNumber, totalBill

    INPUT areaCode

END WHILE

END
