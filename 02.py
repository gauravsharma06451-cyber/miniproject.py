print("SMARTCAMPUS UTILITY & ACCESS PASS GENERATOR")

category = int(input("Select User Category (1: Student, 2: Faculty/Staff): "))

if category == 1:

    subcategory = input("Enter Subcategory (UG/PG): ").upper()

    if subcategory != "UG" and subcategory != "PG":
        print("ERROR: Invalid student subcategory")
        exit()

    cgpa = float(input("Enter Student CGPA (0.0-10.0): "))

    if cgpa < 0 or cgpa > 10:
        print("ERROR: CGPA must be between 0.0 and 10.0")
        exit()

    if subcategory == "UG":
        base_fee = 500
    else:
        base_fee = 350

    merit_discount = 0

    if cgpa >= 8.5:
        merit_discount = base_fee * 20 / 100

    elif cgpa >= 7.5 and cgpa <= 8.49:
        merit_discount = base_fee * 10 / 100


elif category == 2:

    subcategory = input("Enter Subcategory (Resident/Visiting): ").lower()

    if subcategory != "resident" and subcategory != "visiting":
        print("ERROR: Invalid faculty subcategory")
        exit()

    years = int(input("Enter Years of Service: "))

    if years < 0:
        print("ERROR: Years of service cannot be negative")
        exit()

    if subcategory == "resident":
        base_fee = 800
    else:
        base_fee = 1200

    merit_discount = 0

    if years > 10:
        seniority_discount = base_fee * 15 / 100
    else:
        seniority_discount = 0


else:
    print("ERROR: Invalid user category")
    exit()


parking = int(input("Select Parking Permit (0: None, 2: Two-Wheeler, 4: Four-Wheeler): "))

if parking == 0:
    parking_fee = 0
    peak_surcharge = 0
    parking_name = "None"

elif parking == 2:
    parking_fee = 200
    peak_surcharge = 0
    parking_name = "2-Wheeler"

elif parking == 4:
    parking_fee = 600
    parking_name = "4-Wheeler"

    if category == 1:
        peak_surcharge = 150
    else:
        peak_surcharge = 0

else:
    print("ERROR: Invalid parking option")
    exit()


units = float(input("Enter Monthly Electricity Consumption (in kWh): "))

if units < 0:
    print("ERROR: Electricity units cannot be negative")
    exit()


if units <= 100:
    electricity_bill = units * 3 + 50

elif units <= 300:
    electricity_bill = 100 * 3
    electricity_bill = electricity_bill + (units - 100) * 5
    electricity_bill = electricity_bill + 100

elif units <= 500:
    electricity_bill = 100 * 3
    electricity_bill = electricity_bill + 200 * 5
    electricity_bill = electricity_bill + (units - 300) * 7.5
    electricity_bill = electricity_bill + 150

else:
    electricity_bill = 100 * 3
    electricity_bill = electricity_bill + 200 * 5
    electricity_bill = electricity_bill + 200 * 7.5
    electricity_bill = electricity_bill + (units - 500) * 10
    electricity_bill = electricity_bill + 250


if category == 1:
    net_total = base_fee - merit_discount + parking_fee + peak_surcharge
else:
    net_total = base_fee - seniority_discount + parking_fee


total = net_total + electricity_bill


print("\nCALCULATED INVOICE BREAKDOWN")

print("Base Access Pass Fee : ₹", format(base_fee, ".2f"))

if category == 1:
    if merit_discount > 0:
        if cgpa >= 8.5:
            print("Merit Discount (20%) : ₹", format(merit_discount, ".2f"))
        else:
            print("Merit Discount (10%) : ₹", format(merit_discount, ".2f"))
else:
    if seniority_discount > 0:
        print("Seniority Discount (15%) : ₹", format(seniority_discount, ".2f"))

print("Parking Fee (" + parking_name + ") : ₹", format(parking_fee, ".2f"))

if peak_surcharge > 0:
    print("Student Peak Surcharge : ₹", format(peak_surcharge, ".2f"))

print("Net Pass & Parking Total : ₹", format(net_total, ".2f"))

print("Electricity Bill (" + str(units) + " kWh) : ₹", format(electricity_bill, ".2f"))

print("TOTAL MONTHLY PAYABLE : ₹", format(total, ".2f"))
