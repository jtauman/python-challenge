#calculate the following:
        #The total number of months included in the dataset
        #The net total amount of "Profit/Losses" over the entire period
        #The average of the changes in "Profit/Losses" over the entire period
        #The greatest increase in profits (date and amount) over the entire period
        #The greatest decrease in losses (date and amount) over the entire period


import os
import csv

#setting path to the initial file
path = os.path.join("Resources", "budget_data.csv")

#reading file
with open(path, "r", newline = '') as initialfile:

    initialread = csv.reader(initialfile, delimiter = ',')

    #loop through the file
    for row in initialread:
        #count the number of rows - header
        #count = intitalread[1]

        #sum all amounts in "Profit/Losses" column
        #sumtotal = sum  initialread[2]

        #calculate averege change per month in the profit/loss column
        #change = row i+1 - row i
        #average change = mean of change

        #greatest increase in profits
        #find max change
        #if row = maxchange the return initalread[1] + initialread [2]

        #greatest decrease in losses
        #find min change
        #if row = min change then return initialread[1] + initial read [2]

    
    print ("Financial Analsysis")
    print("------------------------")
    print("Total Months: " + str(count))
    print("Total:  $" + str(sumtotal)) 
    print("Average Change:  $" + str(avchange))
    print("Greatest Increase in Profits: " + date + "(" + value + ")")
    print("Greatest Decrease in Profits: " + date + "(" + value + ")")

#setting path for outputfile
summaryfilepath = os.path.join("Resources", "budgetdata_summary.csv")

#writing output to file
with open(summaryfilepath, "w", newline='') as summaryfile:

    summarywrite = csv.writer(summaryfile, delimiter = ",")
    summarywrite.writerow("Financial Analsysis")
    summarywrite.writerow("Total Months: " + str(count))
    summarywrite.writerow("Total:  $" + str(sumtotal)) 
    summarywrite.writerow("Average Change:  $" + str(avchange))
    summarywrite.writerow("Greatest Increase in Profits: " + date + "(" + value + ")")
    summarywrite.writerow("Greatest Decrease in Profits: " + date + "(" + value + ")")
