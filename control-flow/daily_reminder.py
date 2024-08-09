# daily_reminder.py

def main():
    # Prompt for a single task
    task = input("Enter the task description: ").strip()
    
    # Prompt for the task's priority
    while True:
        priority = input("Enter the priority level (high, medium, low): ").strip().lower()
        if priority in {"high", "medium", "low"}:
            break
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

    # Prompt for time sensitivity
    while True:
        time_bound = input("Is this task time-bound? (yes or no): ").strip().lower()
        if time_bound in {"yes", "no"}:
            break
        print("Invalid input. Please enter 'yes' or 'no'.")

    # Provide customized reminder based on priority and time sensitivity
    match priority:
        case "high":
            reminder = f"High priority task: {task}"
        case "medium":
            reminder = f"Medium priority task: {task}"
        case "low":
            reminder = f"Low priority task: {task}"
        case _:
            reminder = "Invalid priority level."

    # Modify reminder if the task is time-bound
    if time_bound == "yes":
        reminder += " — This requires immediate attention today!"

    # Print the reminder
    print(reminder)

if __name__ == "__main__":
    main()

