# Floating-point numbers have limited precision and may not store decimal values exactly.
# leads to unexpected results when performing arithmetic operations.

## case 1 : 1 digit after decimal point
floatNumber = 0.5
extending_Decimal_To_25_Places = format(floatNumber, '.25f')
print(extending_Decimal_To_25_Places)  #0.5000000000000000000000000
# note that 0.5 is printed correctly.


## case 2 : more than 1 digit after decimal point
floatNumber = 0.356
extending_Decimal_To_25_Places = format(floatNumber, '.25f')
print(extending_Decimal_To_25_Places)  #0.3560000000000000156579461
# note that 0.356 is not printed correctly.

# NOTES:
# this can occurs in both case 1 & case 2, but case 2 is more likely to show the issue.
# 0.1+0.2 = 0.30000000000000004 is a classic example of this issue.
# this is not a bug in Python, but a limitation of floating-point arithmetic in computers.
# to avoid such issues, use 'decimal' module, but it is slower than floating-point arithmetic.
