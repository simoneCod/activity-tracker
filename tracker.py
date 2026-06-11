from datetime import date

#funzioni 

#funzione per aggiungere un'attivitá al file data.txt(1)
def add_activity():
      today = date.today()
      name = input("what did you do today?").strip().capitalize()

      with open("data.txt", "a")as file:
             file.write(f"{today} | {name}\n")

             print("Saved!")


#funzione per mostrare le attivitá salvate nel file data.txt(2)
def show_activities():
    try:
        with open("data.txt", "r") as file:
            lines = file.readlines()

        print("\n---- YOUR ACTIVITIES ----")

        if len(lines) == 0:
            print("No activities yet.")
            return

        for i, line in enumerate(lines):
            print(f"{i+1}. {line.strip()}")

    except FileNotFoundError:
        print("No data found yet.")
  

#funzione per eliminare un'attivitá dal file data.txt(3)
def delete_activities():
    try:
        with open("data.txt", "r") as file:
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

        with open("data.txt", "w") as file:
            file.writelines(lines)

        print("Selected activities deleted.")

    except FileNotFoundError:
        print("No data file found.")
            

#funzione per cercare un'attivitá nel file data.txt(4)
def search_activity():
     try:
        with open("data.txt", "r")as file:
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