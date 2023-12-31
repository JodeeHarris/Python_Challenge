import os
import csv
#Values being assigned lists
l_p = []
months = []

#places the path to a value
csvpath = os.path.join("Resources", "budget_data.csv")

#opens the csvfile to allow the program to read the information
with open(csvpath) as csvfile:

    #The Act of reading the file with arguements on how to read the file
    csvreader = csv.reader(csvfile, delimiter=',')
    
    ##Skips the headers
    csv_header = next(csvreader)
    
    # Placing the word values with a numerical value
    previous = 0
    rowcount = 0
    total_sum= 0
    
     # Row accesses our csv list
    for row in csvreader:
        
        #Counts total amount of rows in the csv
        rowcount += 1
        
        #stacks the added values in column 2 to one total number 
        total_sum += int(row[1])
        
        #Sets the first value in Column 2 as the value
        previous = int(row[1])
        
         #conditional "if" statement to not count the first value in the column 
        if rowcount != 1:
            
            #Don't add the first value to your stacking value 
            pl = int(row[1]) - previous
            
            #Adds a single item to the collection type
            l_p.append(pl)
            months.append(row[0])
        
    
            
# Printing results to the terminal    
print("Total Transactions: " + str(rowcount))

print(f"Total: ${total_sum}")

# Creates the average change
avg_lp = sum(l_p) / len(l_p)

#Printing results to the terminal
print(f"Average Change: ${avg_lp:,.2f}")

#The max value
pl_max = max(l_p)

#Searches for the matching value in the list
pl_index_max = l_p.index(pl_max)

#matchs the month with the max value
pl_month_max = months[pl_index_max]

#The max value
pl_min = min(l_p)

#Searches for the matching value in the list
pl_index_min =l_p.index(pl_min)

#matchs the month with the max value
pl_month_min = months[pl_index_min]

#Printing results to the terminal
print(f"Greatest Increase in Profits: {pl_month_max} (${pl_max})")
print(f"Greatest Decrease in Profits: {pl_month_min} (${pl_min})")

#Opening a path to a text file and writing in it with a value to address the folder
with open("Analysis/Info.txt", "w") as output_folder:
    
    #writing in the text file
    output_folder.write("Total Transactions: " + str(rowcount)+ "\n")
    output_folder.write(f"Total: ${total_sum}\n")
    output_folder.write(f"Average Change: ${avg_lp:,.2f}\n")
    output_folder.write(f"Greatest Increase in Profits: {pl_month_max} (${pl_max}) \n")
    output_folder.write(f"Greatest Decrease in Profits: {pl_month_min} (${pl_min}) \n")
