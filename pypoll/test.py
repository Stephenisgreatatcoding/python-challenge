import os
import csv

csvpath = './election_data.csv'

mydict = {}
totvotes = 0

with open(csvpath,'r') as polldata:
    csvreader = csv.reader(polldata)
    next(csvreader)


    for row in csvreader:
        totvotes = totvotes + 1
        if row[2] in mydict.keys():
            mydict[row[2]] = mydict[row[2]] + 1
        else:
            mydict[row[2]] = 1

candidates = []
votecount = []

for key,value in mydict.items():
        candidates.append(key)
        votecount.append(value)

percent = []
for x in votecount:
    percent.append(x/totvotes*100)

    newlist = list(zip(candidates,votecount,percent))

    winnerlist = []

for name in newlist:
    if max(votecount) == name[1]:
        winnerlist.append(name[0])

winner = winnerlist[0]



print(totvotes)
print(candidates)
print(votecount)
print(percent)
print(winner)
