# Filter: Bill Over $10

## Description
Displays customers whose total bill exceeds $10.

## Pseudocode

START

INPUT areaCode

WHILE areaCode != 999

    INPUT phoneNumber
    INPUT messages

    CALL ComputeBill(messages) → totalBill

    IF totalBill > 10 THEN
        DISPLAY areaCode, phoneNumber, totalBill
    END IF

    INPUT areaCode

END WHILE

END
