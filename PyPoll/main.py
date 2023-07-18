import os
import csv

#places the path to a value
csvpath = os.path.join ("Resources", "election_data.csv")

#opens the csvfile to allow the program to read the information
with open(csvpath,'r') as csvfile:
    
    #The Act of reading the file with arguements on how to read the file
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Skips the headers
    csv_header = next(csvreader)
    
    # Placing the word values with a numerical value     
    rowcount = 0
    politician_vote = 0
    counterstockham = 0
    counterdegette = 0
    counterdoane = 0
    x = 0
    
    # Row accesses our csv list
    for row in csvreader:
        
        #Counts total amount of rows in the csv
        rowcount += 1
       
        #Accessing the third column in our csv
        politician_vote = row[2]
        
        #Placing conditional "if" statements to locate this value from column three 
        if politician_vote == "Charles Casper Stockham":
           
            #If value is found add one to the original value until the is no more values to check 
            counterstockham = counterstockham + 1
        
        if politician_vote == "Diana DeGette":
            counterdegette = counterdegette + 1
        
        if politician_vote == "Raymon Anthony Doane":
            counterdoane = counterdoane + 1

#Finding the Percentages of each candidate selected        
per_stockham = (counterstockham / rowcount) * 100
per_degette = (counterdegette / rowcount) * 100
per_doane = (counterdoane / rowcount) * 100
    
#Using "if" statements to locate which candidate had the most counted votes
if counterstockham > counterdoane and counterstockham > counterdegette:
    #Assigning a value to the output
    x = str((f"Winner: Charles Casper Stockham"))

elif counterdegette > counterstockham and counterdegette > counterdoane:
    
    x = str((f"Winner: Diana DeGette"))

elif counterdoane > counterstockham and counterdoane > counterdegette:
    
    x = str((f"Winner: Raymon Anthony Doane"))

#Printing results to the terminal
print("Election Results")

print("-------------------------")

print("Total Votes: " + str(rowcount))

print("-------------------------")

print(f"Charles Casper Stockham: {per_stockham}% ({counterstockham})")
print(f"Diana DeGette: {per_degette}% ({counterdegette})")
print(f"Raymon Anthony Doane: {per_doane}% ({counterdoane})")

print("-------------------------")

print(x)

print("-------------------------")

#Opening a path to a text file and writing in it with a value to address the folder
with open("Analysis/Info.txt", "w") as output_folder:
    
    #writing in the text file
    output_folder.write("Election Results"+ "\n")
    output_folder.write("-------------------------" + "\n")
    output_folder.write("Total Votes: " + str(rowcount) + "\n")
    output_folder.write("-------------------------" + "\n")
    output_folder.write(f"Charles Casper Stockham:{per_stockham}% ({counterstockham})\n")
    output_folder.write(f"Diana DeGette: {per_degette}% ({counterdegette})\n")
    output_folder.write(f"Raymon Anthony Doane:{per_doane}% ({counterdoane})\n")
    output_folder.write(f"-------------------------\n")
    output_folder.write(f"{x}\n")
    output_folder.write(f"-------------------------\n")
   
