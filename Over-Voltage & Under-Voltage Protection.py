# Over-Voltage & Under-Voltage Protection System
# EEE Python Project

# Voltage limits
MIN_VOLTAGE = 210
MAX_VOLTAGE = 250


def voltage_protection(voltage):

    print("\n==============================")
    print(" VOLTAGE PROTECTION SYSTEM")
    print("==============================")

    print(f"Measured Voltage : {voltage:.2f} V")
    print(f"Safe Range       : {MIN_VOLTAGE} - {MAX_VOLTAGE} V")

    # Under-voltage condition
    if voltage < MIN_VOLTAGE:

        print("\n⚠ UNDER-VOLTAGE DETECTED")
        print("Voltage is below the safe limit.")
        print("Protection Status : TRIP")
        print("Load Supply       : OFF")

    # Over-voltage condition
    elif voltage > MAX_VOLTAGE:

        print("\n⚠ OVER-VOLTAGE DETECTED")
        print("Voltage is above the safe limit.")
        print("Protection Status : TRIP")
        print("Load Supply       : OFF")

    # Normal condition
    else:

        print("\n✓ VOLTAGE NORMAL")
        print("Voltage is within the safe range.")
        print("Protection Status : NORMAL")
        print("Load Supply       : ON")


# Main program

print("================================")
print(" OVER/UNDER VOLTAGE PROTECTION")
print("================================")

while True:

    voltage = float(input("\nEnter measured voltage (V): "))

    voltage_protection(voltage)

    choice = input("\nCheck another voltage? (yes/no): ")

    if choice.lower() != "yes":
        print("\nProgram stopped.")
        break
