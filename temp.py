import sys

if len(sys.argv) != 2:
    print("Usage: python temperature.py <temp_in_celsius>")
    sys.exit(1)

temp = float(sys.argv[1])

if temp < 15:
    print("Cold")
elif temp <= 30:
    print("Normal")
else:
    print("Hot")
