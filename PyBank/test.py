#PyBank Challenge - calculate
        #The total number of months included in the dataset
        #The net total amount of "Profit/Losses" over the entire period
        #The average of the changes in "Profit/Losses" over the entire period
        #The greatest increase in profits (date and amount) over the entire period
        #The greatest decrease in losses (date and amount) over the entire period

import os
import csv

#setting path to the initial file
path = os.path.join("Resources", "budget_data.csv")

#setting up lists
date = []
profitloss = []
change = []

#creating function to define average
def average (numbers): 
    return sum(numbers) / len(numbers)

#reading file
with open(path, "r", newline = '') as initialfile:

    initialread = csv.reader(initialfile, delimiter = ',')

    #remover header row
    header = next(initialread) 

    #loop through the file
    for row in initialread:
        
        #loop through rows and append values to appropriate list
        date.append(row[0])
        profitloss.append(int(row[1]))

#obtain the first value of the profitloss list as the seed value
x = profitloss[0]

#rerun through the file to populate the change list, which is change in the profit loss column for each month
with open(path, "r", newline = '') as initialfile:

    initialread = csv.reader(initialfile, delimiter = ',')

    #remover header row
    header = next(initialread) 

    #loop through the file
    for row in initialread:
        #calculate change per month in the profit/loss column
        change.append(int(row[1])-x)
        x = int(row[1])

#sum all amounts in "Profit/Losses" column
sumtotal = sum(profitloss)

print (x)
print (sumtotal)
print (change)

change.pop(0)
mean = round(average(change),2) #average of the change in the profit/loss column
maxprofit = max(change) #max value in the list of change in the profit/loss column
maxindex = change.index(maxprofit) #find the index of the max profit so that the associated date can be found (+1 due to pop in change)
maxloss = min(change) #min value in the list of change in the profit/loss column
lossindex = change.index(maxloss)

print("Financial Analysis")
print("------------------------")
print("Total Months: " + str(len(date))) #count the number of elements in the date list
print("Total:  $" + str(sumtotal)) 
print("Average Change:  $" + str(mean))
print (f'Greatest Increase in Profits: {date[maxindex + 1]}  (${change[maxindex]})')
print (f'Greatest Decrease in Profits: {date[lossindex + 1]}  (${change[lossindex]})')

#setting path for outputfile
summaryfilepath = os.path.join("analysis", "budgetdata_summary2.txt")

#writing output to file
with open(summaryfilepath, "w", newline='') as summaryfile:

    summaryfile.write("Financial Analysis\n")
    summaryfile.write("----------------------------\n")
    summaryfile.write("Total Months: " + str(len(date))+"\n")
    summaryfile.write("Total:  $" + str(sumtotal)+"\n") 
    summaryfile.write("Average Change:  $" + str(mean)+"\n")
    summaryfile.write(f'Greatest Increase in Profits: {date[maxindex + 1]}  (${change[maxindex]})\n')
    summaryfile.write(f'Greatest Decrease in Profits: {date[lossindex + 1]}  (${change[lossindex]})\n')
