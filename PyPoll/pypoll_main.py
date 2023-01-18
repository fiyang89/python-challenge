#data election_data.csv w/ "Ballot ID", "County", "Candidate"
import os 
import csv

csv_path = os.path.join('pypoll_resources','election_data.csv')

#Export text file
output_file = os.path.join('pypoll_final.txt')

#Track empty data
ballot_id = []
county = []
candidate_list = []
total_votes = 0
pct_candidate = []
count_candidate = []
candidates_unique = []

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    #print(csv_header)

    for row in csvreader:
        #Add ballot ID data as string
        ballot_id.append(row[0])

        #Add county data as string
        county.append(row[1])

        #Add candidate data as string
        candidate_list.append(row[2])

        #Calculate the Total Number of Votes cast
        #.sum()?
        total_votes = len(ballot_id)

#open the output file
with open(output_file, "w") as file:
    #write each line in the text file reference: https://www.pythontutorial.net/python-basics/python-create-text-file/
    file.write('Election Results\n')
    file.write('-------------------------------------------------\n')
    file.write(f'Total Votes: {total_votes}\n')
    file.write('-------------------------------------------------\n')

    print('Election Results')
    print('-------------------------------------------------')
    print(f'Total Votes: {total_votes}')
    print('-------------------------------------------------')

    #if candidate matches the next line, skip, but if not, add to candidate_votes list
    #Calculate a complete list of candidates who received votes
    #.unique()?
    name = candidate_list[0]

    for name in candidate_list:
        if name not in candidates_unique:
            candidates_unique.append(name)
               
    #print(candidates_unique)

    #Calculate the total number of votes each candidate won.
    #start with empyt variable for candidate with votes
    candidate_count = 0

    #candidate is currently set to the first name in first row
    candidate = candidate_list[0]
    last_count = 0

    #for a candidate in the list of unique candidates
    for candidate in candidates_unique:

        #look for candidate in unique candidates who has a vote in candidate list
        for vote in candidate_list:

            #if the candidate in unique candidates who has a vote in candidate list has a vote
            if candidate == vote:

                #add it
                candidate_count += 1

        #Calculate the percentage of votes each candidate won
        #candidate votes/total votes = % rounded to .000 decimals
        percent = round(float(candidate_count) / float(len(candidate_list)) * 100, 3)

        #add percent for each unique candidat w/ votes to pct candidate list
        pct_candidate.append(percent)

        #add number of votes to count_candidate list
        count_candidate.append(candidate_count)

        #Calculate the winner of the election based on popular vote
        #.max(above variable) & index
        #if the last candidate votes are less than a calculated (n) candidate count, the winner with the highest candidate count is the candidate
        if last_count < candidate_count:
            Winner = candidate

        candidate_results = (f'{candidate}: {percent}% ({candidate_count})')
        print(candidate_results)
        print('-------------------------------------------------')

        file.write(f'{candidate_results}\n')
        file.write('-------------------------------------------------\n')

        #Reset last vote counts and all other candidate counts
        last_count = candidate_count
        candidate_count = 0
    
    print(f"Winner: {Winner}")
    print('-------------------------------------------------')

    file.write(f'Winner: {Winner}\n')
    file.write('-------------------------------------------------\n')





