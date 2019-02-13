import os
import csv

# Path to collect data from the Resources folder
Pypollcsvreader = os.path.join('election_data.csv')

# Read in the CSV file
with open(Pypollcsvreader, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip Header         
    next(csvreader)
    # List to pull the VoterID
    lists = []
    # List to pull the Votername
    votersnames = []
    # List to store Distinct voternames
    Disvoterlist = []


      
    for row in csvreader:
        # Assign voterid to variable
        voterid = row[0]
        # Assign candidate to variable
        Names = row[2]
       
        #append voterid to list
        lists.append(voterid)
        #append candidate to list
        votersnames.append(Names)
#print to Election Results with total count        
print("Election Results")
print("---------------------------")
print(f"Total Votes: {len(lists)}")
print("---------------------------")


Pypollcsvwriter = os.path.join('ouput.csv')

with open(Pypollcsvwriter, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow("---------------------------")
    csvwriter.writerow("Election Results")
    csvwriter.writerow(["---------------------------"])
    csvwriter.writerow("---------------------------")
    csvwriter.writerow(f"Total Votes: {len(lists)}")
    csvwriter.writerow("---------------------------")

# Define a function to send a list of candidates to get count
def candidatevotecount(Candidate):
    counter = 0
    for x in votersnames:
        if (x == Candidate):
            counter += 1

     
    print(["f{Candidate}: {(round((counter/len(votersnames) * 100),0))}% ({counter})"])
    return counter
    

   
Setval = set(votersnames)
Sortedset = sorted(Setval)

winner = 0

for y in Sortedset:
    votecountereturn = candidatevotecount(y)
    # print Candidate vote counts and percentage        
    # csvwriter.writerow([f"{y}: {(round((votecountereturn/len(votersnames) * 100),0))}% ({votecountereturn})"])
    

    if votecountereturn > winner:
        winner = votecountereturn
        Cand = y
print("---------------------------")
print(f"Winner: {Cand}")
print("---------------------------")
# csvwriter.writerow("---------------------------")
# csvwriter.writerow(f"Winner: {Cand}")
# csvwriter.writerow("---------------------------")



    


