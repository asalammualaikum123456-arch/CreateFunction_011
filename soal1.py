def convert_temperature(value, unit):
    unit = unit.upper()
    if unit == 'C':
        return (value * 9/5) + 32
    elif unit == 'F':
        return (value - 32) * 5/9
    else:
        return "Unit tidak valid. Harap masukkan 'C' atau 'F'."

print("100 C = ", convert_temperature(100, 'C'), "F")
print("212 F = ", convert_temperature(212, 'F'), "C")