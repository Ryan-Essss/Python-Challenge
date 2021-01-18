import os
import csv

csvpath = os.path.join ('Resources','election_data.csv')
# print(csvpath)

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)
    # print(type(csvreader))

    # Reads header row first
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Set CSV variables
    total_votes = 0
    khan_votes = 0
    correy_votes = 0 
    li_votes = 0 
    tool_votes = 0
    winner = ""


    # Read each row for the  votes
    for row in csvreader:
        if str(row[2]) == "Khan":
            khan_votes += 1
        if str(row[2]) == "Correy":
            correy_votes += 1
        if str(row[2]) == "Li":
            li_votes += 1
        if str(row[2]) == "O'Tooley":
            tool_votes += 1

total_votes = khan_votes+correy_votes+li_votes+tool_votes

# Fiding out who won
if (khan_votes > correy_votes and khan_votes > li_votes and khan_votes > tool_votes):
    winner = "Khan"

elif(correy_votes > khan_votes and correy_votes > li_votes and correy_votes > tool_votes):
    winner = "Correy"

elif(li_votes > khan_votes and li_votes > correy_votes and li_votes > tool_votes):
    winner = "Li"

elif(tool_votes > khan_votes and tool_votes > correy_votes and tool_votes > li_votes):
    winner = "O'Tooley"
    
else:
    winner = "Would you look at that, We have a tie!"

# print(khan_votes)
# print(correy_votes)
# print(li_votes)
# print(tool_votes)
# print(total_votes)
# print(winner)

khan_percent = round((khan_votes/total_votes),3)*100
correy_percent = round((correy_votes/total_votes),3)*100
li_percent = round((li_votes/total_votes),3)*100
# Unsure why the Li vote percentage is outputting incorrectly
tool_percent = round((tool_votes/total_votes),3)*100
# print(khan_percent)

# Prints in the terminal
print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------------")
print(f"Khan: {khan_percent}% ({khan_votes})")
print(f"Correy: {correy_percent}% ({correy_votes})")
print(f"Li: {li_percent}% ({li_votes})")
# Unsure why the Li vote percentage is outputting incorrectly
print(f"O'Tooley: {tool_percent}% ({tool_votes})")
print("----------------------------------------")
print(f"Winner: {winner}")
print("----------------------------------------")

# Showed issues rounding / unsure why
# print(f"Khan: {round((khan_votes/total_votes),2)*100}% ({khan_votes})")
# print(f"Correy: {round((correy_votes/total_votes),2)*100}% ({correy_votes})")
# print(f"Li: {round((li_votes/total_votes),2)*100}% ({li_votes})")
# print(f"O'Tooley: {round((tool_votes/total_votes),2)*100}% ({tool_votes})")

# Creates or writes or whatever to a .txt file
f = open("Analysis\\analysis.txt", 'w')
f.write("Election Results\n")
f.write("----------------------------------------\n")
f.write(f"Total Votes: {total_votes}\n")
f.write("----------------------------------------\n")
f.write(f"Khan: {khan_percent}% ({khan_votes})\n")
f.write(f"Correy: {correy_percent}% ({correy_votes})\n")
f.write(f"Li: {li_percent}% ({li_votes})\n")
f.write(f"O'Tooley: {tool_percent}% ({tool_votes})\n")
f.write("----------------------------------------\n")
f.write(f"Winner: {winner}\n")
f.write("----------------------------------------")
f.close()


# Previous code used to output txt
# f = open("Analysis\\analysis.txt", 'w')
# f.write("Election Results\n")
# f.write("----------------------------------------\n")
# f.write(f"Total Votes: {total_votes}\n")
# f.write("----------------------------------------\n")
# f.write(f"Khan: {round((khan_votes/total_votes),2)*100}% ({khan_votes})\n")
# f.write(f"Correy: {round((correy_votes/total_votes),2)*100}% ({correy_votes})\n")
# f.write(f"Li: {round((li_votes/total_votes),2)*100}% ({li_votes})\n")
# f.write(f"O'Tooley: {round((tool_votes/total_votes),2)*100}% ({tool_votes})\n")
# f.write("----------------------------------------\n")
# f.write(f"Winner: {winner}\n")
# f.write("----------------------------------------")
# f.close()
