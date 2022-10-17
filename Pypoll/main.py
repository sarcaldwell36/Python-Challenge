
import os
import csv


PyPollcsv = os.path.join("/Users/sarahcaldwell/Library/CloudStorage/OneDrive-Personal/Penn/Homework","election_data.csv")



with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
   
    count = 0
    candidate_list = []
    unique_candidate = []
    count_votes = []
    percent_votes = []
    
    for row in csvreader:
        count = count + 1
        candidate_list.append(row[2])
        # list of names of candidates (unique)
    
    for x in set(candidate_list):
        unique_candidate.append(x)
       
        y = candidate_list.count(x)
        count_votes.append(y)
      
        z = (y/count)*100
        percent_votes.append(z)
        
    winning_vote_count = max(count_votes)
    winner = unique_candidate[count_votes.index(winning_vote_count)]
    
 
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            new_percent_votes = [f'{item:.3f}' for item in percent_votes]
            new_unique_candidate = sorted(unique_candidate)
            print(new_unique_candidate[i] + ": " + str(new_percent_votes[i]) +"% (" + str(count_votes[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")


with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        new_percent_votes = [f'{item:.3f}' for item in percent_votes]
        new_unique_candidate = sorted(unique_candidate)
        text.write(new_unique_candidate[i] + ": " + str(new_percent_votes[i]) +"% (" + str(count_votes[i])+ ")")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")

