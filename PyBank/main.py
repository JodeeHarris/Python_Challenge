""" 

1. The total number of months included in the dataset

2. The net total amount of "Profit/Losses" over the entire period

3. The changes in "Profit/Losses" over the entire period, and then 
the average of those changes

4. The greatest increase in profits (date and amount) over the entire period

5. The greatest decrease in profits (date and amount) over the entire period 

6. In addition, your final script should both print the analysis to the terminal 
and export a text file with the results.

"""
import os
import csv

l_p = []
months = []

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    
    previous = 0
    rowcount = 0
    total_sum= 0
    for row in csvreader:
        rowcount += 1
        total_sum += int(row[1])
        if rowcount != 1:
            pl = int(row[1]) - previous
            l_p.append(pl)
            months.append(row[0])
            
        previous = int(row[1])
            
    
print("Total Transactions: " + str(rowcount))

print(f"Total: ${total_sum}")

avg_lp = sum(l_p) / len(l_p)

print(f"Average Change: ${avg_lp:,.2f}")

pl_max = max(l_p)
pl_index_max = l_p.index(pl_max)
pl_month_max = months[pl_index_max]

pl_min = min(l_p)
pl_index_min =l_p.index(pl_min)
pl_month_min = months[pl_index_min]

print(f"Greatest Increase in Profits: {pl_month_max} (${pl_max})")
print(f"Greatest Decrease in Profits: {pl_month_min} (${pl_min})")

with open("Analysis/Info.txt", "w") as output_folder:
    
    output_folder.write("Total Transactions: " + str(rowcount)+ "\n")
    output_folder.write(f"Total: ${total_sum}\n")
    output_folder.write(f"Average Change: ${avg_lp:,.2f}\n")
    output_folder.write(f"Greatest Increase in Profits: {pl_month_max} (${pl_max}) \n")
    output_folder.write(f"Greatest Decrease in Profits: {pl_month_min} (${pl_min}) \n")
""" 
for profit in l_p[1]:
    
     if float(profit) >= 0:
         
        profit_sum = sum(profit)
         


for loss in l_p[1]:
    
    if float(loss) < 0:
        
        loss_sum = sum(loss)



def average(profit):
    
    length_p = len(profit)
    counter_p = 0 
       
    for ProAvg in profit:
       
        counter_p = counter_p + ProAvg
        counter_p = counter_p + 1
            
        avg_p = counter_p / length_p     
        
        return avg_p
       
       
def average(loss):
    
    length_l = len(loss)
    counter_l = 0

    for LossAvg in profit:
       
        counter_l = counter_l + LossAvg
        counter_l = counter_l + 1
            
        avg_l = counter_l / length_l
        
        return avg_l

 #how to get average rate  of change?
 #  """

""" amount_max = []
amount_min = []
for temp in csvreader:
    amount_max = 
 """
