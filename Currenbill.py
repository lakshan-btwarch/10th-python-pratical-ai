# Code to calculate the electricity bill
consumer_number = int(input("Enter Consumer Number: "))
power_consumed = int(input("Enter Power Consumed (in units): "))

if 0 <= power_consumed <= 100:
    bill_amount = power_consumed * 1
elif 101 <= power_consumed <= 300:
    bill_amount = 100 + (power_consumed - 100) * 1.25
elif 301 <= power_consumed <= 500:
    bill_amount = 350 + (power_consumed - 300) * 1.50
elif power_consumed > 500:
    bill_amount = 650 + (power_consumed - 500) * 1.75
else:
    print("Invalid Power Consumed Units")
    bill_amount = 0

print("\n\tABC Power Company Ltd.")
print("~" * 40)
print(f"Consumer Number: {consumer_number}")
print(f"Consumed Units: {power_consumed}")
print(f"Bill Amount: Rs. {bill_amount:.2f}")
