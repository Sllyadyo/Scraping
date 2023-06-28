from Parser import parse_data
from prettytable import PrettyTable


def display_table(table_data):
    table = PrettyTable()
    # Table header
    table.field_names = ["Apr 2023", "Apr 2022", "Programming Language", "Ratings", "Change"]
    
    # Adding rows to a table
    for row in table_data:
        table.add_row([row["Apr 2023"], row["Apr 2022"], row["Programming Language"], row["Ratings"], row["Change"]])
        
    print(table)


while True:
    print("""Menu:
1. Load top 20 programming languages
2. Update information from the table
3. Exit the program  
""")
    
    try:
        answer = int(input('Please enter a number: '))
        
        if answer == 1 or answer == 2:
            data = parse_data()      # Getting data from the parsing function
            
            if data:
                display_table(data)   # Displaying a table with data
                
                if answer == 1:
                    continue          # We continue the cycle to display the menu again after displaying the table
                    
                elif answer == 2:
                    print("Updating information...\n")
                    
                    new_data = parse_data()   # Updating table information 
                    
                    if new_data is not None:  
                        data = new_data         # If the data is successfully updated, we replace the old data with new ones
                        
                        print("Information updated.\n")
                        
                        display_table(data)     # Displaying the updated table
                    
                    else:
                        print("Failed to update information. Please try again.\n")
                    
                    continue          # We continue the cycle to display the menu again after updating the information
                    
            else:                     # If the data is not received or empty, we output an error message
                print("Failed to load data. Please try again.\n")
                continue
                
        elif answer == 3:
            break                    # Exiting the loop and the program
        
        else:
            print("Please enter a number between 1 and 3.\n")

    except ValueError:
        print("Invalid input. Please enter a number.\n")