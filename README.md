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

  INSTRUCTIONS: Create a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is
  composed of two column: "Date" and "Profit/Losses".
  
  TASKS: Calculate the total number of months included in the dataset. Calculate the net total amount of "Profit/Losses" over the entire period. Calculate the changes 
  in "Profit/Losses" over the entire period. Calculate the average of those changes. Calculate the greatest increase in profits (date and amount) over the entire 
  period. Calculate the greatest decrease in profits (date and amount) over the entire period. Export a text file with the results.

  GETTING STARTED: 
  
    1. Import csv and os
    2. Create a path to the csv file
    3. Create variables:
       ballot_id = []
       county = []
       candidate_list = []
       total_votes = 0
       pct_candidate = []
       count_candidate = []
       candidates_unique = []
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
