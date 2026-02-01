def validate_time(time_str):
    """Validate HH:MM format and business hours"""
    try:
        h, m = map(int, time_str.split(':'))
        if 9 <= h <= 18 and 0 <= m <= 59:
            return f"{h:02d}:{m:02d}"
        return None
    except:
        return None


def store_patient_records():
    """Task 1: Store validated patient appointments"""
    appointments = []
    n = int(input("Enter number of appointments: "))
    for i in range(n):
        print(f"\nPatient {i + 1}:")
        while True:
            name = input("Name: ").strip()
            if name: break
            print("Name cannot be empty!")

        while True:
            dept = input("Department (Cardiology/Orthopedics/Neurology): ").strip()
            if dept in ['Cardiology', 'Orthopedics', 'Neurology']: break
            print("Invalid department!")

        while True:
            time_input = input("Time (HH:MM): ").strip()
            valid_time = validate_time(time_input)
            if valid_time:
                appointments.append((name, dept, valid_time))
                break
            print("Invalid time! Use HH:MM (09:00-18:00)")

    return appointments


def maintain_department_lookup():
    """Task 2: Department lookup dictionary"""
    return {
        "Cardiology": "Cardiology-Heart Care (Dr. Patel)",
        "Orthopedics": "Orthopedics-Bone & Joint Care (Dr. Singh)",
        "Neurology": "Neurology-Brain & Nerve Care (Dr. Gupta)"
    }


def display_all_appointments(appointments, dept_lookup):
    """Display all appointments"""
    print("\nAll Appointments:")
    print("----------------------------------")
    for app in appointments:
        print(f"{app[2]} | {dept_lookup.get(app[1], app[1])} | {app[0]}")
    print("----------------------------------")


def filter_appointments_by_dept(appointments, dept_lookup):
    """Task 3: Filter and sort by department"""
    search_dept = input("\nEnter department to filter: ").strip()
    filtered = [app for app in appointments if app[1].lower() == search_dept.lower()]
    filtered.sort(key=lambda x: x[2])  # Sort by time

    print(f"\n{dept_lookup.get(search_dept.title(), search_dept.title())} Appointments (sorted):")
    print("----------------------------------")
    if filtered:
        for app in filtered:
            print(f"{app[2]} - {app[0]}")
    else:
        print("No appointments found.")
    print("----------------------------------")


def generate_summary(appointments):
    """Task 4: Summary statistics"""
    dept_counts = {}
    for app in appointments:
        dept_counts[app[1]] = dept_counts.get(app[1], 0) + 1

    print("\nSummary Statistics:")
    total = len(appointments)
    busiest = max(dept_counts.items(), key=lambda x: x[1], default=("None", 0))

    for dept, count in sorted(dept_counts.items()):
        print(f"{dept}: {count}")
    print(f"{busiest[0]}: {busiest[1]} (Busiest)")
    print(f"Total: {total}")


def main():
    """Task 5: Modular execution"""
    try:
        appointments = store_patient_records()
        dept_lookup = maintain_department_lookup()

        display_all_appointments(appointments, dept_lookup)
        filter_appointments_by_dept(appointments, dept_lookup)
        generate_summary(appointments)

    except KeyboardInterrupt:
        print("\nProgram terminated.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
