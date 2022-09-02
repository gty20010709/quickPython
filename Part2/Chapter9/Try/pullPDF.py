#!/bin/python
# pullPDF.py - Pull all PDF file from ~ to current working dir.

import shutil
import os

filesPath = []

for path,subnames,filenames in os.walk('/home/theo/'):
    print(path)
    # for filename in filenames:
        # if filename.endswith('.pdf') or filename.endswith('.PDF'):
        #     filePath = os.path.join(path,filename)
        #     print(filePath)

    

#  Loop whole dir.

# TODO Find all PDF.

# TODO Get the path.

# TODO Move PDF file.