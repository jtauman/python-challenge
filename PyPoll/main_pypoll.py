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
        
#A unique list of candidates who received votes
        if row[2] not in uniquecandidate:
            uniquecandidate.append(row[2])


totalvotes = int(len(voterID))

#def electionresults():
    #for x , y in candidate_dict.items():
       # print(x + ": " + str(round(y/totalvotes*100, 2)) + "%  (" + str(y) + ")")

#The total number of votes each candidate won
#create a dictionary, count the occurrence of each candidate for each candidate(l) in the set (candidate)
candidate_dict = dict((l, candidate.count(l)) for l in set(candidate))

print("Election Results")
print("------------------------")
print("Total Votes: " + str(totalvotes))
print("------------------------")
# for each key value pair, print key(x), %of votes ((round(y/totalvotes*100, 2)) and total votes (y)
for x , y in candidate_dict.items():
    print (x + ": " + str(round(y/totalvotes*100, 2)) + "%  (" + str(y) + ")")

print("------------------------")

#The winner of the election based on popular vote. 
#getting the key from the maximum value
keymax = max(candidate_dict, key=candidate_dict.get)
print("Winner: " + keymax)
print("------------------------")


#write to file
#setting path for outputfile
summaryfilepath = os.path.join("analysis", "electiondata_summary.txt")

#writing output to file
with open(summaryfilepath, "w", newline='') as summaryfile:

    summaryfile.write("Election Results\n")
    summaryfile.write("------------------------\n")
    summaryfile.write("Total Votes: " + str(totalvotes) + "\n")
    summaryfile.write("------------------------\n")
    for x , y in candidate_dict.items():
        summaryfile.write(x + ": " + str(round(y/totalvotes*100, 2)) + "%  (" + str(y) + ")\n")
    summaryfile.write("------------------------\n")
    summaryfile.write("Winner: " + keymax + "\n")
    summaryfile.write("------------------------\n")
