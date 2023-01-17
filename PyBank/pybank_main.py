#Create a script to analyze financial records
#Use budget_data.csv (put it in your resources folder). Has "Date" & "Profit/Losses"
import os
import csv

csv_path = os.path.join('pybank_resources','budget_data.csv')

#Track empty data
profit = []
months = []
total_months = 0
total_net = 0

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

    for row in csvreader:
        #Add date data as string
        months.append(row[0])

        #Add profit data as string
        profit.append(int(row[1]))
        
        #Calculate the Total number of Months included in the dataset
        #Possibly a .count() and .unique()
        total_months = (len(months))

        #Calculate the Net Total Amount of Profit/Losses over the entire period
        #.sum()?
        total_net = sum(profit)

        #Calculate the Changes in Profit/Losses over the entire period
        #Difference = profit - losses
        profit_change = []

        #for a number in range 1-profit count
        for x in range(1,len(profit)):
            #add data from current profit number - previous profit number
            profit_change.append(int(profit[x]) - int(profit[x-1]))
 
            #Calculate the greatest increase in profits (date & amount) over the entire period
            #.max()
            greatest_increase = max(profit_change)
            #position in row[1] of greatest increase. How do you connect it to the month in row[0]?
            month_increase = profit_change.index(greatest_increase) + 1
            greatest_increase_month = months[month_increase]
        
            #Calculate the greatest decrease in profits
            #.min()
            greatest_decrease = min(profit_change)
            month_decrease = profit_change.index(greatest_decrease) + 1
            greatest_decrease_month = months[month_decrease]

            #Calculate the average of those changes .mean()
            profit_average = round(sum(profit_change) / len(profit_change), 2)

    #Print
    print('Financial Analysis')
    print('-------------------------------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total Net: ${total_net}')
    print(f'Average Change: ${profit_average}')
    print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')

#Export text file
output_file = os.path.join('pybank_final.txt')

output_lines = ['Financial Analysis', '-------------------------------------------------', f'Total Months: {total_months}', f'Total Net: ${total_net}', f'Average Change: ${profit_average}', f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})', f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})']
#open the output file
with open(output_file, "w") as file:

    #write the header row
    file.write('\n'.join(output_lines))