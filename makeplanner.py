#!/usr/bin/env python3
import sys, calendar, re, datetime, pandas
from PyPDF2 import PdfFileMerger
sys.setrecursionlimit(1500)

###SET CUSTOM PDF FILES HERE###
month_pdf = 'month.pdf'
week_pdf = 'week.pdf'
day_pdf = 'day.pdf'

###BEGIN INPUT SANITISATION###

#Check arg lenth
if len(sys.argv) != 3 and len(sys.argv) != 4:
    print("Script expects arguments: year,  month, [filename]")
    exit()

#Check first 2 args are numbers
bad_request = False
try:
    year = int(sys.argv[1])
except:
    print("Year is not a number")
    bad_request = True
    
try:
    month = int(sys.argv[2])
except:
    print("Month is not a number")
    bad_request = True

if bad_request:
    exit()

#Check month and day are in limits
bad_request = False
if year < 2018 or year > 2100:
    print("Year should be between 2018 and 2100")
    bad_request = True
if month < 1 or month > 12:
    print("Month should be between 1 and 12")
    bad_request = True

if bad_request:
    exit()

#Output name sanitise/creation
outputname = ""
if len(sys.argv) == 4:
    outputname = sys.argv[3]
    #Remove trailing .pdf's
    while outputname.endswith(".pdf"):
        outputname = outputname[:-4]
    #Only allowed characters
    outputname = re.sub('[^a-zA-Z0-9_-]+', '', outputname)
    if outputname == "":
        print("Invalid output name")
        exit()
    if len(outputname) > 30:
        print("Max output name length is 30 characters")
        exit()
    outputname += ".pdf"
else:
    outputname = "Planner-%s-%d.pdf" % (calendar.month_name[month], year)

###END INPUT SANITISATION###
###BEGIN LOGIC###

#Start and end range
range_start = datetime.date(year, month, 1)
range_end = datetime.date(year, month, calendar.monthrange(year, month)[1])

daterange = pandas.date_range(range_start, range_end)

try:
    merger = PdfFileMerger()
    merger.append(month_pdf)

    for d in daterange:
        if d.weekday() == 0:
            merger.append(week_pdf)
        merger.append(day_pdf)

    merger.write(outputname)
    print("Wrote " + outputname)
except Exception as e:
    print("Something went wrong: " + str(e)) 
