#!/bin/python
# renameDates.py - Rename filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import shutil
import os
import re

# create a regex that matches files with the American date formate.
datePattern = re.compile(r'''^(.*?)
        ((0|1)?\d)-         # one or two digits for the month
        ((0|1|2|3)?\d)-      # one or two digits for the day
        ((19|20)\d\d)       # for digitis for the year
        (.*?)$
        ''',re.VERBOSE)

# Loop over the files in the working direcrory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    # Skip files without a date.
    if mo == None:
        continue
    # Get the different parts fo the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(7)
    afterPart = mo.group(8)

    #  Form the European-style filename.
    euroFilename = beforePart + dayPart+ '-'  + monthPart + '-' + yearPart + afterPart

    #  Get the full, absolute file paths.
    absWrokingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWrokingDir,amerFilename)
    euroFilename = os.path.join(absWrokingDir,euroFilename)

    # Rename the files.
    # print('Renameing "%s" to "%s" ...'%(amerFilename,euroFilename))
    shutil.move(amerFilename,euroFilename)







