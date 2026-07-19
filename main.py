from tracker import (
    add_activity,
    delete_activities,
    search_activity,
    show_activities,
)


def main() -> None:
    """Run the Activity Tracker command-line menu."""

    while True:
        choice = input(
            """
1 - Add activity
2 - Show activities
3 - Delete activity
4 - Search activity
10 - Exit

Choose an option: """
        ).strip()

        if choice == "1":
            add_activity()
        elif choice == "2":
            show_activities()
        elif choice == "3":
            delete_activities()
        elif choice == "4":
            search_activity()
        elif choice == "10":
            print("Exit...")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()