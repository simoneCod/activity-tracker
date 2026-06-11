from tracker import *


# variabile ciclo while
running = True 

#menú
while running:
    scelta = input("""
 1 - add activity
 2 - show activities
 3 - delete activity
 4 - search activity
 10 - exit  
                                              
 """)

    #scelta che termina il programma
    if scelta == "10":
         print("Exit...")
         running = False

    #scelta che aggiuunge un'attivitá al file data.txt
    elif scelta == "1":
            add_activity()

    #scelta che mostra le attivitá salvate nel file data.txt
    elif scelta == "2":
            show_activities()

    #eliminazione di un'attivitá dal file data.txt
    elif scelta == "3":
            delete_activities()

    #ricerca di un'attivitá nel file data.txt
    elif scelta == "4":
            search_activity()   
            



    #scelta che gestisce l'input non valido
    else:
        print("invalid option")
  