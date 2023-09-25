import os
import csv

csvpath = "C:/Users/DeMiko Birden/Desktop/homework/python-challenge/PyPoll/Resources/election_data.csv"
file_to_output = "election_results.txt"

total_votes = 0
candidates = []
candidate_votes = {}
winner_count = 0
winner = ""

# First loop to count total votes
with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        total_votes += 1

# Write election results
with open(file_to_output, 'w') as txt_file:
    election_header = (
        f"Election Results\n"
        f"---------------\n")
    txt_file.write(election_header)
    
    with open(csvpath) as csvfile:  # Re-open CSV file
        csvreader = csv.DictReader(csvfile)

        for row in csvreader:
            candidate = row["Candidate"]
            if candidate not in candidates:
                candidates.append(candidate)
                candidate_votes[candidate] = 1
            
            candidate_votes[candidate] += 1

        for candidate in candidate_votes:
            votes = candidate_votes[candidate]
            vote_percentage = (votes / total_votes) * 100
            voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
            txt_file.write(voter_output)

            if votes > winner_count:
                winner_count = votes
                winner = candidate

        winning_summary = (
            f"---------------\n"
            f"Winner: {winner}\n"
            f"---------------\n"
        )
        txt_file.write(winning_summary)

    total_votes_output = f"Total Votes: {total_votes}\n"
    txt_file.write(total_votes_output)
