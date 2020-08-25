"""Electricity Bill"""
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity Bill Estimator")
choice = int(input("Which tariff? 11 or 31: "))
while choice != 11 and choice != 31:
    print("Invalid tariff")
    choice = int(input("Which tariff? 11 or 31: "))

if choice == 11:
    cents_per_kwh = TARIFF_11 * 100
elif choice == 31:
    cents_per_kwh = TARIFF_31 * 100

daily_use = int(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

estimated_bill = (cents_per_kwh / 100) * daily_use * billing_days
print(f"Estimated bill: ${estimated_bill}")
