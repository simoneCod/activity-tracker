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
def delete_activities():
    try:
        with open(DATA_FILE, "r") as file:
            lines = file.readlines()

        if len(lines) == 0:
            print("No activities to delete.")
            return

        print("\n---- YOUR ACTIVITIES ----")

        for i, line in enumerate(lines):
            print(f"{i+1}. {line.strip()}")

        choices = input("\nEnter numbers to delete (e.g. 1,3,5): ")
        raw_choices = choices.split(",")

        valid_choices = []

        for c in raw_choices:
            c = c.strip()

            if c.isdigit():
                num = int(c)

                if 1 <= num <= len(lines):
                    valid_choices.append(num)
                else:
                    print(f"Warning: {num} does not exist")
            else:
                print(f"Warning: '{c}' is not a number")

        if len(valid_choices) == 0:
            print("No valid selections. Nothing deleted.")
            return

        for index in sorted(valid_choices, reverse=True):
            lines.pop(index - 1)

        with open(DATA_FILE, "w") as file:
            file.writelines(lines)

        print("Selected activities deleted.")

    except FileNotFoundError:
        print("No data file found.")
            

#funzione per cercare un'attivitá nel file data.txt(4)
def search_activity():
     try:
        with open(DATA_FILE, "r")as file:
             lines = file.readlines()
        
        if len(lines) == 0:
             print("No activities to search.")
             return
        
        search_result = []
        search = input("Enter the activity that you're loking for: ").strip().lower()

        for line in lines:
             if search in line.lower(): 
                 search_result.append(line)
         
        if len(search_result) == 0:
             print("No matching activities found.")
             return     
        
        print("\n---- SEARCH RESULTS ----")
        print("Found", len(search_result), "activities \n")

        for activities in search_result:
          print(activities.strip())
        
      

     except FileNotFoundError:
         print("No data file found.")  