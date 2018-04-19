#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import shutil as sh
import collections

# verbose output:
debug = False

def helper():
    print("")
    print("Usage: python filesort.py [OPTION] [DIR]")
    print("Sort files from DIR (the current directory by default) into")
    print("subdirectories.")
    print("")
    print("This program creates folders containing files of one kind.")
    print("With the kind defining the folder's name.")
    print("")
    print("Currently it has no options and only works on the local dir ;-)")

# inform the user:
helper()

# the potential candidates:
direntries = os.listdir('./')

#
# Create list of file extensions - with corresponding filenames
#

# Remove directories from current direntries
files = []
for direntry in direntries:
        curFile = os.path.splitext(direntry)
        if curFile[1] != '':
            files.append(curFile)
            if debug:
                print(curFile)

# Find unique extensions
extensions = set()
for s in files:
    if s[1] not in extensions:
        extensions.add(s[1])
extensions = [x.lower() for x in extensions]

print("")
print("Filetypes identified:")
print(extensions)
print("")

#
# Create dirs by extension
# - if not possible: use extension in uppercase
# - convert space to under
#

# Prepare folders where files with extensions will be sorted into
folders = collections.defaultdict()

folders['archives'] = {'.zip', '.gz', '.tgz', '.rar', '.dmg', '.tar', '.pkg'}
folders['databases'] = {'.sql', '.json'}
folders['docs'] = {'.tex', '.doc', '.dot', '.docm', '.docx', '.rtf', '.odt', '.odm', '.ott', '.txt', '.md', '.html', '.htm'}
folders['images'] = {'.png', '.gif', '.jpg', '.jpeg', '.svg', '.xcf', '.eps'}
folders['spreadsheets'] = {'.ods', 'ots', '.xls', '.xlsx', '.csv'}
folders['dfs'] = {'.pdf', '.ps', '.skim', '.djvu', '.epub'}
folders['presentations'] = {'.ppt', '.pptx', '.odp', '.otp', '.pez', '.keynote', '.key'}
folders['videos'] = {'.avi', '.mp4', '.mpg', '.mkv', '.flv', '.mov'}
folders['audios'] = {'.mp3', '.wav', '.ogg'}

if debug:
    for foldername, extset in folders.items():
        print("### " + foldername)
        for ext in extset:
            print(ext, end="")
        print("")

for foldername, extset in folders.items():
    for ext in extset:
        # Create directories for found files/extensions
        if ext in extensions:
            if not os.path.exists('_'+foldername):
                os.mkdir('_'+foldername)
    # Move files into folders
    for file in files:
        if file[1].lower() in extset:
            sh.move(file[0]+file[1], '_'+foldername+'/'+file[0]+file[1])

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
