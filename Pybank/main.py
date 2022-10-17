#pybank

import os
import csv
os.getcwd

PyBankcsv = os.path.join("/Users/sarahcaldwell/Library/CloudStorage/OneDrive-Personal/Penn/Homework","budget_data.csv")





with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    profit = []
    monthly_changes = []
    date = []

 
    count = 0
    total_profit = 0
    total_change = 0
    start_profit = 0
    
    
    for row in csvreader:    
      # # of months
      count = count + 1 

      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      #trouble with average change in profits, class example didn't work?
      def average(numbers):
        length = len(numbers)
        total_profit = 0.0
        for number in numbers:
          total_profit += number
        return total_profit / length 

      #print(average)


      #another way of doing average but still not correct?
      end_profit = int(row[1])
      monthly_change_profits = end_profit - start_profit

      monthly_changes.append(monthly_change_profits)

      new_total_change = total_change + monthly_change_profits
      start_profit = end_profit

      average_change = (new_total_change/count)
      
     #greatest increase and decrease
      date.append(row[0])

      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase_profits)]
      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
      
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")


