# python-challenge

PYBANK 

  INSTRUCTIONS: Create a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is
  composed of two column: "Date" and "Profit/Losses".
  
  TASKS: Calculate the total number of months included in the dataset. Calculate the net total amount of "Profit/Losses" over the entire period. Calculate the changes 
  in "Profit/Losses" over the entire period. Calculate the average of those changes. Calculate the greatest increase in profits (date and amount) over the entire 
  period. Calculate the greatest decrease in profits (date and amount) over the entire period. Export a text file with the results.

  GETTING STARTED: 
  
    1. Import csv and os
    2. Create a path to the csv file
    3. Create variables:
       profit = []
       months = []
       total_months = 0
       total_net = 0
    4. Open the csv file and code for skiping the header row
    5. Use a for loop to add the Date and Profit/Losses data from the csv file into the variables
    6. Calculate the total months using len(). First task complete.
    7. Calculate the net total amount using sum(). Second task complete.
    8. Create a profit_change = [] variable
    9. Using a for loop, find a number within the range for profit
    10. Add data from the current profit data minus the previous profit data also known as the change/difference
    11. Calculate the greatest increase with the max() function
    12. Index the greatest increase in profit_change to associate the date and amount. Third task complete.
    13. Repeat steps 11 & 12 to calculate the greatest decrease. Fourth task complete.
    14. Calculate the average change using basic math: sum of profit_change / total count of profit_change
    15. Print results
    16. Export results to a text file using output_file
  
  FOR FURTHER HELP: Reference www.stackoverflow.com, www.pythontutorial.net/python-basics/python-create-text-file/
  
  PROJECT CONTRIBUTORS: Steffi Yang
  
 
  ______________________________________________________________________________________________________________________________________________________
  

PYPOLL 

  INSTRUCTIONS: Create a Python script to analyze the votes to help a small, rural town modernize its vote-counting process. You will be given a set of poll data 
  called election_data.csv.
  
  TASKS: Calculate the total number of votes cast. Calculate a list of candidates who received votes. Calculate the percentage of votes for each candidate. 
  Calculate the total number of votes for each candidate. Calculate the winner of the election based on popular vote.

  GETTING STARTED: 
  
    1. Import csv and os
    2. Create a path to the csv file
    3. Create an output file path 
    4. Create variables:
       ballot_id = []
       county = []
       candidate_list = []
       total_votes = 0
       pct_candidate = []
       count_candidate = []
       candidates_unique = []
    5. Open the csv file and code for skiping the header row
    6. Use a for loop to add the ballot ID, county, and candidates data from the csv file into the variables
    7. Calculate the total votes using len() and print the total. First task complete.
    8. To make exporting less of a hassle, open the output file here and start writing the Total Votes. 
    9. Calculate the list of unique candidates by creating a variable called name = [] and setting it equal to the first value in the candidate list
    10. Using a for loop, search for a name in the candidate list. 
    11. Using an if statement, add the name from the candidate list that is not in the new candidate_unique list. Second task complete.
    12. Calculate the votes per candidate by setting a new variable, candidate_count = 0. Then, set a new variable, candidate equal to the first value in the 
        candidate list. Finally, set a new variable, last_count = 0.
    13. Using a for loop, find a candidate in the list of unique candidates
    14. Within that loop, use another for loop to look for a unique candidate who has a vote in candidate list. Use an if statement to test if a candidate has a 
        vote, then add it to the candidate_count
    15. Calculate the percentage by using the candidate_count value and dividing it by the candidate list count. Multiply by 100.
    16. Add each percent value by appending it to a new list. Third task complete.
    17. Calculate the number of candidate votes by adding the candidate_count to a new list. Fourth task complete.
    18. Now, use another if statement to determine the winner. The last candidates vote counts should be less than the candidate vote counts so the winner is equal 
        to the candidate from the unique candidate list. Fifth task complete.
    19. Create a new variable candidate_results that contains candidate, percent, and candidate_count. Print.
    20. Write the output file line for the list of candidates containing candidate name, percent, and vote count using candidate_results 
    21. Reset all values for the last count and candidate count
    22. Print the winner
    23. Write the output file line for the winner.
  
  FOR FURTHER HELP: Reference www.stackoverflow.com, www.pythontutorial.net/python-basics/python-create-text-file/
  
  PROJECT CONTRIBUTORS: Steffi Yang
