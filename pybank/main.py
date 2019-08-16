import os
import csv
import sys
sys.stdout = open("./stats.txt", "w")

csvpath = './budget_data.csv'

bankdata = open(csvpath)
csvreader = csv.reader(bankdata)
next(csvreader)

allrows = []


for row in csvreader:
    mydict = {}
    mydict['month'] = row[0]
    mydict['pl'] = int(row[1])
    
    allrows.append(mydict)

def getmonths():
    return len(allrows)

def gettotpl():
    pl = 0
    for row in allrows:
        pl = pl + row['pl']
    return pl
         
def getavechang():
    summonthchang = 0
    for i in range(1,len(allrows),1):
        currpl = (allrows[i]['pl'])
        prevpl = (allrows[i-1]['pl'])
        monthpl = currpl - prevpl
        summonthchang = summonthchang + monthpl
    monthlychang = summonthchang/(getmonths()-1)
    return monthlychang

def getmaxmonth():
    monthdifflist = []
    currentmax = -999999999999999
    currentmonth = None

    for i in range(1,len(allrows),1):
        currpl = (allrows[i]['pl'])
        prevpl = (allrows[i-1]['pl'])
        diffmonthpl = currpl - prevpl
        if diffmonthpl > currentmax:
            currentmax = diffmonthpl
            currow = allrows[i]
            currentmonth = currow['month']
    return [ currentmonth, currentmax ]

def getminmonth():
    monthdifflist = []
    currentmin = 999999999999999
    currentmonth = None

    for i in range(1,len(allrows),1):
        currpl = (allrows[i]['pl'])
        prevpl = (allrows[i-1]['pl'])
        diffmonthpl = currpl - prevpl
        if diffmonthpl < currentmin:
            currentmin = diffmonthpl
            currow = allrows[i]
            currentmonth = currow['month']
    return [ currentmonth, currentmin ]

print('Total months = ', getmonths())
print('Net ProfitLoss = ', gettotpl())
print('Average Change = ', getavechang())
print('Biggest increase month = ', getmaxmonth())
print('Biggest decrease month = ', getminmonth())

