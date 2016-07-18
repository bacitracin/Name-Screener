# Name-Screener
Screens CSVs  with social media posts and identifies the rows that begin with a name ('tagging')

This script is meant to screen out FB posts that are just mentions of names.

How to use:
Babynames.csv is a CSV with ~6,600 baby names. Save this file to your Python directory.
Add any new names you encounter to the bottom of the sheet.
For your sentiment file, save a CSV file with just the FB posts 
(no header, just copy & paste from SimplyMeasured). Edit the name of the file
at the bottom (last line)
Get back: a CSV file with the following columns:
    1. Original FB post
    2. First word of the post
    3. Is the first word of the post a name?
    4. Is the entire post >= 5 words? (Indicates additional commentary past name...)
