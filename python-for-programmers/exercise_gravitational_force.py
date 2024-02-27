G = 6.67 * (10 ** -11)
M = 6.0 * (10 ** 24)  # Mass of Earth
m = 7.34 * (10 ** 22)  # Mass of the moon
r = 3.84 * (10 ** 8)

# Write your code here

# Calculation of the base number
# The result has to be divided by 10 in order to be in cientific notation
grav_force_base = round(((667 * 6 * 734) / 384 ** 2) / 10, 2)

# Calculation of the exaponent number
# Because the base number was divided by 10,
# The exponent has to have - 1
grav_force_exponent = (-13 + 24 + 20) - (8 + 2) - 1

print(f"{grav_force_base} * 10^{grav_force_exponent}")