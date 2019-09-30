#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# # to European DD-MM-YYYY.

import shutil
import os
import re


os.chdir('/Users/jishuyanfa-ios/Desktop/语音视频调研')
# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?)     # all text before the date
    ((0|1)?\d)-                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day
    ((19|20)\d\d)                   # four digits for the year
    (.*?)$                          # all text after the date
    """, re.VERBOSE)

# 01-03-2014capital20190617.txt
# ('', '01', '0', '03', '0', '2014', '20', 'capital20190617.txt')

# datePattern = re.compile(r"""^(1)
# (2 (3) )-
# (4 (5) )-
# (6 (7) )
# (8)$
# """, re.VERBOSE)

# TODO: Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    # Skip files without a date.
    if mo is None:
        continue

    print(mo.group())
    print(mo.groups())
    # Get the different parts of the filename.
    beforePart = mo.group(1)  # ‘’
    monthPart = mo.group(2)  # ‘01’
    dayPart = mo.group(4)    # ‘03’
    yearPart = mo.group(6)   # ‘2014 ’
    afterPart = mo.group(8)  # ‘capital20190617.txt’

    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    # Rename the files.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)  # uncomment after testing
