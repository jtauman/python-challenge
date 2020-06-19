import os
import csv

#setting path to the initial file
path = os.path.join("Resources", "election_data.csv")

#setting up lists
voterID = []
candidate = []

#reading file
with open(path, "r", newline = '') as initialfile:

    initialread = csv.reader(initialfile, delimiter = ',')

    #remover header row
    header = next(initialread) 

    #loop through the file
    for row in initialread:

    #The total number of votes cast
        voterID.append(row[0])


#A complete list of candidates who received votes


#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.

print("Election Results")
print("------------------------")
print("Total Votes: " + str(len(voterID)))
print("------------------------")
#print("Total Months: " + str(len(date))) #count the number of elements in the date list
#print("Total:  $" + str(sumtotal)) 
#print("Average Change:  $" + str(mean))
#print (f'Greatest Increase in Profits: {date[maxindex + 1]}  (${change[maxindex]})')
#print (f'Greatest Decrease in Profits: {date[lossindex + 1]}  (${change[lossindex]})')