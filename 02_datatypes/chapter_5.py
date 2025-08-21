import sys
from fractions import Fraction
ideal_temp = 95.5

current_temp = 95.4999999

print(f"Ideal Temp {ideal_temp}")
print(f"Current  Temp {current_temp}")
print(f"Diff Temp {ideal_temp-current_temp}")
print(sys.float_info)
print(Fraction(ideal_temp).limit_denominator())
print(Fraction(current_temp).limit_denominator())
