# Compute Bill Module

## Description
Calculates the total bill based on number of messages sent.

## Pseudocode
```
START

INPUT messages

pretax = 5.00

IF messages > 100 THEN
    IF messages <= 300 THEN
        pretax = pretax + ((messages - 100) * 0.03)
    ELSE
        pretax = pretax + (200 * 0.03)
        pretax = pretax + ((messages - 300) * 0.02)
    END IF
END IF

afterTax = pretax * 1.14

RETURN afterTax

END
```
