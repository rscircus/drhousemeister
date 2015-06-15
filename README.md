# Dr. House Meister

This bunch of scripts **organize/sort/refile the files in your current
folder** into newly created folders according to their extensions.

It was created to clean up my *Downloads* folder from time to time.


## Usage:

```
cd /path/to/dir/to/be/cleaned
ln -s /path/to/drhousemeister/filesort.py
./filesort.py
```


## Supported files:

These folders are created in the current directory and contain, what
you might expect:

* _audios - *mp3 so far*
* _archives - *most common ones*
* _databases - sql, json
* _documents - *linux, win*
* _images - *most common ones*
* _dfs - pdf (*including skim<sup>1</sup> notes*), ps, odf
* _presentations - *linux, win, mac*
* _tables - *linux, win*


## Changelog:

### [0.1.1] - 2015.06.15
Added:
- filesort.py - presentations, archives, databases, audio, var. extensions

Fixed:
- filesort.py - .docx extension bug in set

Changed:
- filesort.py - pdfs, extensions

### [0.1] - 2015.06.14
Created:
- filesort.py - refile files as described in read.me


## Genesis Note:

This started out in bash while scratching my own itch. However, I
switched to python as things became way to complicated in bash and the
program has already twice the functionality with half the lines of code
in its initial state.


## Footnotes:

1: http://skim-app.sourceforge.net/
