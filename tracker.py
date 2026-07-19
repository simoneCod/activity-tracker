from datetime import date

DATA_FILE = "data.txt"


#funzione per aggiungere un'attivitá al file data.txt(1)
def add_activity() -> None:
    """Ask the user for an activity and save it with today's date."""

    activity_name = input("What did you do today? ").strip()

    if not activity_name:
        print("Activity cannot be empty.")
        return

    today = date.today()

    with open(DATA_FILE, "a", encoding="utf-8") as file:
        file.write(f"{today} | {activity_name}\n")

    print("Activity saved!")


#funzione per mostrare le attivitá salvate nel file data.txt(2)
def show_activities() -> None:
    """Display all saved activities."""

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            activities = file.readlines()
    except FileNotFoundError:
        print("No activities found yet.")
        return

    if not activities:
        print("No activities yet.")
        return

    print("\n---- YOUR ACTIVITIES ----")

    for index, activity in enumerate(activities, start=1):
        print(f"{index}. {activity.strip()}")
  

#funzione per eliminare un'attivitá dal file data.txt(3)
def delete_activities() -> None:
    """Delete one or more saved activities by their displayed number."""

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            activities = file.readlines()
    except FileNotFoundError:
        print("No activities found yet.")
        return

    if not activities:
        print("No activities to delete.")
        return

    print("\n---- YOUR ACTIVITIES ----")

    for index, activity in enumerate(activities, start=1):
        print(f"{index}. {activity.strip()}")

    raw_choices = input(
        "\nEnter activity numbers to delete (for example 1,3,5): "
    ).strip()

    if not raw_choices:
        print("No selection entered.")
        return

    valid_indexes = set()

    for choice in raw_choices.split(","):
        choice = choice.strip()

        if not choice.isdigit():
            print(f"Warning: '{choice}' is not a valid number.")
            continue

        activity_number = int(choice)

        if not 1 <= activity_number <= len(activities):
            print(f"Warning: activity {activity_number} does not exist.")
            continue

        valid_indexes.add(activity_number - 1)

    if not valid_indexes:
        print("No valid selections. Nothing deleted.")
        return

    remaining_activities = [
        activity
        for index, activity in enumerate(activities)
        if index not in valid_indexes
    ]

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        file.writelines(remaining_activities)

    print(f"Deleted {len(valid_indexes)} activity or activities.")
            

#funzione per cercare un'attivitá nel file data.txt(4)
def search_activity() -> None:
    """Search saved activities by keyword."""

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            activities = file.readlines()
    except FileNotFoundError:
        print("No activities found yet.")
        return

    if not activities:
        print("No activities to search.")
        return

    keyword = input("Enter an activity to search for: ").strip().lower()

    if not keyword:
        print("Search term cannot be empty.")
        return

    matching_activities = [
        activity
        for activity in activities
        if keyword in activity.lower()
    ]

    if not matching_activities:
        print("No matching activities found.")
        return

    print(f"\n---- SEARCH RESULTS ({len(matching_activities)}) ----")

    for activity in matching_activities:
        print(activity.strip())