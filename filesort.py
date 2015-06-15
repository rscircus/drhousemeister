#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import shutil as sh

debug = False

def helper():

    print ""
    print "Usage: python filesort.py [OPTION] [DIR]"
    print "Sort files from DIR (the current directory by default) into"
    print "subdirectories."
    print ""
    print "This program creates folders containing files of one kind."
    print "With the kind defining the folder's name."
#    print ""
#    print "Optionally the files can further be sorted by year."
#    print ""


#
# MAIN
#

# inform the user:
helper()

# the potential candidates:
direntries = os.listdir('./')

#
# Create list of file extensions - with corresponding filenames

# Sort out directories:
files = []
for direntry in direntries:
        curFile=os.path.splitext(direntry)
        if curFile[1]!='':
            files.append(curFile)
            if debug:
                print curFile

# Find unique extensions:
extensions = set()
for s in files:
    if s[1] not in extensions:
        extensions.add(s[1])

# Lower case:
extensions = [x.lower() for x in extensions]

print ""
print "Filetypes identified:"
print extensions
print ""

#
# Create dirs by extension
# - if not possible: use extension in uppercase
# - convert space to under
#

# This is pretty hacky. Most file managers sort the _ ahead of everything else
docs = {'.tex', '.doc', '.dot', '.docm', '.docx', '.rtf', '.odt', '.odm', '.ott', '.txt'}
spreadsheets = {'.ods', 'ots', '.xls', '.xlsx', '.csv'}
images = {'.png', '.gif', '.jpg', '.jpeg', '.svg', '.xcf'}
archives = {'.zip', '.gz', '.tgz', '.rar' }
presentations = {'.ppt', '.pptx', '.odp', '.otp', '.pez', '.keynote'}
#videos = {'.avi', '.mp4' '.mpg', '.mkv'}
pdfs = {'.pdf', '.skim'}

for doc in docs:
    if doc in extensions:
        if not os.path.exists('_documents'):
            os.mkdir('_documents')

for spreadsheet in spreadsheets:
    if spreadsheet in extensions:
        if not os.path.exists('_spreadsheets'):
            os.mkdir('_spreadsheets')

for image in images:
    if image in extensions:
        if not os.path.exists('_images'):
            os.mkdir('_images')

for archive in archives:
    if archive in extensions:
        if not os.path.exists('_archives'):
            os.mkdir('_archives')

for presentation in presentations:
    if presentation in extensions:
        if not os.path.exists('_presentations'):
            os.mkdir('_presentations')

for pdf in pdfs:
    if pdf in extensions:
        if not os.path.exists('_pdfs'):
            os.mkdir('_pdfs')


# Move files into dirs
for file in files:
    if file[1].lower() in docs:
        sh.move(file[0]+file[1], '_documents/'+file[0]+file[1])
    if file[1].lower() in spreadsheets:
        sh.move(file[0]+file[1], '_spreadsheets/'+file[0]+file[1])
    if file[1].lower() in images:
        sh.move(file[0]+file[1], '_images/'+file[0]+file[1])
    if file[1].lower() in archives:
        sh.move(file[0]+file[1], '_archives/'+file[0]+file[1])
    if file[1].lower() in presentations:
        sh.move(file[0]+file[1], '_presentations/'+file[0]+file[1])
    if file[1].lower() in pdfs:
        sh.move(file[0]+file[1], '_pdfs/'+file[0]+file[1])


#TODO: If more than one "year" present than create folders with year
#
# e.g.:
#
# ~/_spreadsheets/2013
# ~/_spreadsheets/2014
# ~/_spreadsheets/2015
#
#
#TODO: If keyword present -> create folder with keyword
# - sort files into keyword
#
# e.g.:
#
# ~/_spreadsheets/KEYWORD/2013
# ~/_spreadsheets/KEYWORD/2014
