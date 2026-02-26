# Filter: Messages Over 100

## Description
Displays only customers who sent more than 100 messages.

## Pseudocode

START

INPUT areaCode

WHILE areaCode != 999

    INPUT phoneNumber
    INPUT messages

    CALL ComputeBill(messages) → totalBill

    IF messages > 100 THEN
        DISPLAY areaCode, phoneNumber, totalBill
    END IF

    INPUT areaCode

END WHILE

END
