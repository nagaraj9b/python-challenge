import os
import csv

# Path to collect data from the Resources folder
PyBankcsvreader = os.path.join('Resources','budget_data.csv')

# Read in the CSV file
with open(PyBankcsvreader, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

           
    next(csvreader)
    lists = []
    Profitloss= []
    list1 = []
    comblist = []


    
    for row in csvreader:
    # To get the Total Months
        Months = row[0]
        lists.append(Months)
    
    #count of total
        Ttal = row[1]
        Profitloss.append(int(Ttal))
    #appending to lists1

    #average of change
    
    
    for i in range(len(lists)-1):
        Prev = Profitloss[i+1] - Profitloss[i]
        xy = lists[i+1]
        list1.append(Prev)
        comblist.append([xy,Prev])
    
    for n in range(len(lists)-1):
        if(max(list1) == comblist[n][1]):
            pos = comblist[n][0]
        if(min(list1) == comblist[n][1]):
            pos1 = comblist[n][0]

PyBankcsvwriter = os.path.join('ouput.csv')

with open(PyBankcsvwriter, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Date","Profit/Loss","profit/loss_change"])
    csvwriter.writerow([lists[0],Profitloss[0],0])
    for wr in range(len(lists)-1):
        csvwriter.writerow([comblist[wr][0],Profitloss[wr+1],comblist[wr][1]])




print("Financial Analysis")
print("------------------")
print(f"Total Months: {len(lists)}")
print(f"Total: $ {sum(Profitloss)}")
print(f'Average  Change: ${round(sum(list1)/85,2)}')
print(f'Greatest Increase in Profits: {pos} (${max(list1)})')
print(f'Greatest Decrease in Profits: {pos1} (${min(list1)})')
