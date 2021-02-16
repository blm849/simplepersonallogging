# simplepersonallogging

## Introduction

I wanted a way to simply log information in a spreadsheet, so I created this logging program.
## File Listing

- easylog.ini:  this provides input to easylog.py. There are three variables: two are prompts for the users
and one is the name of the XLSX file to append to
- easylog.py: this is the actual Python program. I run it using python easylog.py. If you want to use a different
ini file, pass the name to to the program
- easylog.xlsx: This is the XLSX file the python program appends to

## Info

You can make the prompts whatever you want in the INI file. But you can only have two unless you change the code.
You can use any spreadsheet you want, just specify the name in the INI file

When you run the program, enter either:

category, comment

or 

category, comment, subcategory

For example, I could enter:

lunch, tuna sandwich
work, completed this repo, projectX

The first entry logs what I ate. The second one logs what I worked on, but also associated it with projectX

This python program goes into a loop until you enter a blank line.


Other files in this repo:
- LICENSE
- README.md

For more information, see the comments section of the Python programs.

