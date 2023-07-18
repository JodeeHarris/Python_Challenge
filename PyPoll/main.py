""" 
1. The total number of votes cast

2. A complete list of candidates who received votes

3. The percentage of votes each candidate won

4. The total number of votes each candidate won

5.The winner of the election based on popular vote 

6. In addition, your final script should both print the analysis 
to the terminal and export a text file with the results.

"""
import os
import csv

poll = []

csvpath = os.path.join ("Resources", "election_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)


print("Election Results")

print("-------------------------")

rowcount = 0

for row in csvreader:
        rowcount += 1
    
print("Total Votes: " + str(rowcount))

print("-------------------------")

for polls in csvreader:
    
    politician_vote = int(poll[2])
    counterstockham = 0
    counterdegette = 0
    counterdoane = 0

    if politician_vote == "Charles Casper Stockham":
        counterstockham == counterstockham + 1
        
    if politician_vote == "Diana DeGette":
        counterdegette == counterdegette + 1
        
    if politician_vote == "Raymon Anthony Doane":
        counterdoane == counterdoane + 1
        
per_stockham = (counterstockham / rowcount) * 100
per_degette = (counterdegette / rowcount) * 100
per_doane = (counterdoane / rowcount) * 100
    

for winner in politician_vote:
    
    if counterstockham > counterdoane and counterstockham > counterdegette:

        
       x = print(f"Winner: Charles Casper Stockham")

    if counterdegette > counterstockham and counterdegette > counterdoane:
    
       x = print(f"Winner: Diana DeGette")

    if counterdoane > counterstockham and counterdoane > counterdegette:
    
       x = print(f"Winner: Raymon Anthony Doane")

print(f"Charles Casper Stockham:{per_stockham}% {counterstockham}")
print(f"Diana DeGette: {per_degette}% {counterdegette}")
print(f"Raymon Anthony Doane:{per_doane}% {counterdoane}")

print("-------------------------")



print("-------------------------")

with open("Analysis/Info.txt", "w") as output_folder:
    
    output_folder.write("Election Results"+ "\n")
    output_folder.write("-------------------------" + "\n")
    output_folder.write("Total Votes: " + rowcount + "\n")
    output_folder.write("-------------------------" + "\n")
    output_folder.write(f"Charles Casper Stockham:{per_stockham}% {counterstockham}\n")
    output_folder.write(f"Diana DeGette: {per_degette}% {counterdegette}\n")
    output_folder.write(f"Raymon Anthony Doane:{per_doane}% {counterdoane}\n")
    output_folder.write(f"-------------------------\n")
    output_folder.write(f"{x}\n")
    output_folder.write(f"-------------------------\n")
   
