import menu_functions
import sys
menu_choice=0
while menu_choice != 3:
    print('-----------------------------')
    print("|Enter 1 for Medicine menu  |")
    print('----------------------------')
    print('|Enter 2 for Customer menu  |')
    print('----------------------------')
    print('|Enter 3 to Quit the program|')
    print('-----------------------------')
    menu_choice=int(input("Enter Your Choice\n"))
    if menu_choice==1:
        menu_functions.medicine_menu()
    elif menu_choice==2:
        menu_functions.customer_menu()
    elif menu_choice==3:
        break
    else:
        print("Invalid Input! Try Again! \n")    
sys.exit()
