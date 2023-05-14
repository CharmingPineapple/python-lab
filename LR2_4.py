# Вариант 17. Отформатировать число 31415.926 в виде: |31,415.926000 |.

print("31415.926")
keyStick = '|'
keyComma = ','
print("{stick}31{comma}415.926{zero}{space}{stick}".format(stick='|', comma=',', zero='000', space=' '))

