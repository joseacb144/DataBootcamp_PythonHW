import csv
import os

# Assigns file path to 'csvpath'
csvpath = os.path.join('election_data_2.csv')

# n_count ('n' represents candidate name) is used to keep count of how many votes each candidate gets.
# Candidate's name can be changed when running script for other candidates.
khan_count = 0
correy_count = 0
li_count = 0
otooley_count = 0

# Opens 'csvfile' and is then assigned as 'readCSV'
with open(csvpath, newline='') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    
    # Starts a for loop that reads all the rows in csv file
    for row in readCSV:
      
    # Sum up all the votes for Khan. n_count
        if row[2] == "Khan":
            khan_count = khan_count + 1
    
    # Sum up all the votes for Correy. n_count
        elif row[2] == "Correy":
            correy_count = correy_count + 1
        
    # Sum up all the votes for Li. n_count    
        elif row[2] == "Li":
            li_count = li_count + 1
        
    # Sum up all the votes for O'Tooley. n_count
        elif row[2] == "O'Tooley":
            otooley_count = otooley_count + 1

    total_votes = khan_count + correy_count + li_count + otooley_count


# n_per is used to get the percentage of votes each candidate has.
# Candidate's name can be changed when running script for other candidates.
khan_per = round(khan_count/total_votes * 100)
correy_per = round(correy_count/total_votes *100)
li_per = round(li_count/total_votes * 100)
otooley_per = round(otooley_count/total_votes * 100)

winner_list = {"Khan" : khan_count, "Correy" :correy_count, "Li" : li_count, "O'Tooley" : otooley_count}
winner = max(winner_list, key=winner_list.get)

print("\n")
print("Election Results")
print("------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Khan: {khan_per}% ({khan_count})")
print(f"Correy: {correy_per}% ({correy_count})")
print(f"Li: {li_per}% ({li_count})")
print(f"Otooley: {otooley_per}% ({otooley_count})")
print("------------------------")
print(f"Winner: {winner}")
print("------------------------")
