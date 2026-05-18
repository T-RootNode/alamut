####################################################
# Thing 02 - 18.05.2025
#
# WHAT I LEARNED:
#   - if / elif / else — branching based on conditions
#   - == is comparison, = is assignment
#   - convert input() result once with int(), then reuse the variable
#
####################################################

z = input("bitte eine zahl ein geben")
x = int(z)
if x > 10:
    print("größer als 10")
elif x == 10:
    print("es ist 10")
else:
    print("kleiner als 10")
