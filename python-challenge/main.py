import pandas as pd

# load csv file
db1 = pd.read_csv('PyBank/Resources/budget_data.csv')

# calculate the total number of months included in the dataset
mnth_tot = len(db1)

# Calculate net total amount of "Profit/Losses"- entire period
tot_net_prof = db1['Profit/Losses'].sum()

# Calculate changes in "Profit/Losses"- entire period
prof_changes = db1['Profit/Losses'].diff()

# Calculate average of those changes
avg_prof_change = prof_changes.mean()

# Calculate the greatest increase in profits (date and amount)- entire period
grtst_increase = prof_changes.idxmax()
grtst_increase_date = db1.loc[grtst_increase, 'Date']
grtst_increase_amt = prof_changes.max()

# Calculate the greatest decrease in profits (date and amount)- entire period
grtst_decrease = prof_changes.idxmin()
grtst_decrease_date = db1.loc[grtst_decrease, 'Date']
grtst_decrease_amt = prof_changes.min()

# Print results
print("\n\tFinancial Analysis \n -----------------------------")
print("Total number of months:", mnth_tot)
print(f"Net total amount of Profit/Losses: ${tot_net_prof}")
print(f"Average profit change:, ${avg_prof_change:,.2f}")
print(f"Greatest increase in profits:", grtst_increase_date, ": ($", grtst_increase_amt, ")")
print(f"Greatest decrease in profits:", grtst_decrease_date, ": ($", grtst_decrease_amt, ")")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

db2 = pd.read_csv('PyPoll/Resources/election_data.csv')

# Calculate the total number of votes cast
tot_vote = len(db2)

# Get a complete list of candidates who received votes
candidates = db2['Candidate'].unique()

# Calculate votes percentage per candidate
candidate_votes = db2['Candidate'].value_counts()
candidate_percentages = (candidate_votes / tot_vote) * 100

# Calculate vote total per candidate
candidate_votes = db2['Candidate'].value_counts()

# Determine the winner of the election based on popular vote
winner = candidate_votes.idxmax()

# Print the results
print("\n\n\n\nElection Results")
print("-----------------------------")
print(f"Total Votes: {tot_vote}")
print("-----------------------------")
for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-----------------------------")
print(f"Winner: {winner}" )
print("-----------------------------")