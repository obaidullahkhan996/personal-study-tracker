
import json
import os

print("===== PERSONAL STUDY TRACKER =====")

# Load existing study records
if os.path.exists("study_records.json"):
    with open("study_records.json", "r") as file:
        study_records = json.load(file)
else:
    study_records = []

# Main menu
while True:
    print("\n===== MENU =====")
    print("1. Add Study Record")
    print("2. View Study Records")
    print("3. Show Total Study Hours")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add a study record
    if choice == "1":
        subject = input("Enter subject name: ")

        try:
            hours = float(input("Enter study hours: "))

            if hours <= 0:
                print("Study hours must be greater than zero!")
                continue

        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        record = {
            "subject": subject,
            "hours": hours
        }

        study_records.append(record)

        # Save records to JSON file
        with open("study_records.json", "w") as file:
            json.dump(study_records, file, indent=4)

        print("Study record added successfully!")

    # View all study records
    elif choice == "2":
        print("\n===== YOUR STUDY RECORDS =====")

        if len(study_records) == 0:
            print("No study records found.")
        else:
            for number, record in enumerate(study_records, start=1):
                print(
                    f"{number}. Subject: {record['subject']} | "
                    f"Hours: {record['hours']}"
                )

    # Calculate total study hours
    elif choice == "3":
        total_hours = 0

        for record in study_records:
            total_hours += record["hours"]

        print(f"\nTotal Study Hours: {total_hours}")

    # Exit the program
    elif choice == "4":
        print("Thank you for using Personal Study Tracker!")
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice! Please select 1, 2, 3, or 4.")
