# Activity Tracker

A Python command-line application for recording and managing daily activities.

The application stores activities in a local text file and provides a simple menu for adding, viewing, searching and deleting entries.

## Features

- Add an activity with the current date.
- Display all saved activities.
- Search activities by keyword (case-insensitive).
- Delete one or more activities by their displayed numbers.
- Persist data in a local text file.
- Handle missing data files and invalid menu or activity input.

## Requirements

- Python 3
- No third-party packages required.

## Getting Started

Clone the repository:

```bash
git clone https://github.com/simoneCod/activity-tracker.git
cd activity-tracker
```

Run the application:

```bash
python main.py
```

On some systems, the command may be:

```bash
python3 main.py
```

The application creates `data.txt` in the project directory when the first activity is saved. The file is intentionally excluded from version control through `.gitignore`, so personal activity data is not committed.

## Menu

```text
1  - Add activity
2  - Show activities
3  - Delete activity
4  - Search activity
10 - Exit
```

## Project Structure

```text
activity-tracker/
├── main.py
├── tracker.py
├── data.example.txt
├── .gitignore
└── README.md
```

- `main.py` contains the command-line menu and application entry point.
- `tracker.py` contains the functions for adding, displaying, deleting and searching activities.
- `data.example.txt` provides sample activity entries for reference; the application uses `data.txt` for its own data.
- `.gitignore` excludes local data and Python-generated files.

## Concepts Practiced

- Python functions and modules.
- Loops and conditional statements.
- Lists and list comprehensions.
- User input and basic validation.
- Reading and writing text files.
- Exception handling.
- Separating the menu from application logic.

## Possible Improvements

- Add categories for activities.
- Allow existing activities to be edited.
- Introduce automated tests.
- Improve validation and data handling.
- Evaluate JSON or SQLite as alternative storage formats.

## Author

**Simone Serio**
