import os
import csv

#setting path to the initial file
path = os.path.join("Resources", "election_data.csv")

#setting up lists
voterID = []
candidate = []
uniquecandidate = []
candidatetotal = []
count0 = 0

#reading file
with open(path, "r", newline = '') as initialfile:

    initialread = csv.reader(initialfile, delimiter = ',')

    #remover header row
    header = next(initialread) 

    #loop through the file
    for row in initialread:

    #The total number of votes cast
        voterID.append(row[0])
        candidate.append(row[2])
        
#A complete list of candidates who received votes
        if row[2] not in uniquecandidate:
            uniquecandidate.append(row[2])


#The percentage of votes each candidate won


#The total number of votes each candidate won

#for item in candidate:
    #candidatetotal.append(uniquecandidate.count)    
#The winner of the election based on popular vote.

totalvotes = int(len(voterID))
print([ [l, candidate.count(l)] for l in set(candidate)])
candidate_dict = dict((l, candidate.count(l)) for l in set(candidate))
print (candidate_dict)

print("Election Results")
print("------------------------")
print("Total Votes: " + str(totalvotes))
print("------------------------")

for x , y in candidate_dict.items():
    print (x + ": " + str(round(y/totalvotes*100, 2)) + "%  (" + str(y) + ")")

print("------------------------")


#print(str(candidatetotal))
#print(candidate[0] + str(count0))
#print("Total:  $" + str(sumtotal)) 
#print("Average Change:  $" + str(mean))
#print (f'Greatest Increase in Profits: {date[maxindex + 1]}  (${change[maxindex]})')
#print (f'Greatest Decrease in Profits: {date[lossindex + 1]}  (${change[lossindex]})')