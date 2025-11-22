import sys

if len(sys.argv) < 2:
    print("Usage: python temp_check.py <temperature>")
    sys.exit(1)


    temperature = float(sys.argv[1])
except ValueError:
    print("Please provide a valid number for temperature.")
    sys.exit(1)


if temperature < 15:
    print("Cold")
elif 15 <= temperature <= 30:
    print("Normal")
else:
    print("Hot")
