# -*- coding: utf-8 -*-
"""
Created on Mon May 18 16:01:30 2015
@author: Tracy

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

"""

import csv
names_set = set()

# Builds names_set. Use the CSV 'babynames.csv' 
def build_the_names_set(filename):
    with open(filename, 'r') as fd:
        for row in fd:
            names_set.add(row)
        fd.close()


# Opens the sentiment CSV and compares the first word of the post with
# names in the names_set. Writes results to a new CSV.
def compare_file_for_names(filename):
    name_status_list = [] 
    first_word_list = []
    full_post_list = []
    more_than_just_name_list = []
    
    with open(filename, 'r') as fd:
        for row in fd:
            full_post = row.strip('\n')
            full_post_in_words = full_post.split()
            first_word = (full_post_in_words[0])
            if (first_word + '\n') in names_set:
                name_status = 'Yes'
            else:
                name_status = 'No'
            if len(full_post_in_words) >= 5:
                more_than_just_name_status = 'Yes'
            else: 
                more_than_just_name_status = 'No'
            first_word_list.append(first_word)          
            name_status_list.append(name_status)
            full_post_list.append(full_post)
            more_than_just_name_list.append(more_than_just_name_status)
            
    full_post_list[0] = 'Full FB post'
    first_word_list[0] = 'First word of FB post'
    name_status_list[0]= 'Is the first word a name?'
    more_than_just_name_list[0]= 'Is the post >= 5 words?'
    
    zipped_list = zip(full_post_list, first_word_list, name_status_list, more_than_just_name_list)  
    fd.close()
 
 # Writes a new CSV with the posts & status
    with open('cleaned_sentiment_file.csv', 'wb') as fd:
        writer = csv.writer(fd)
        writer.writerows(zipped_list)
        fd.close()

          
build_the_names_set('babynames.csv')

# Edit the name of the sentiment file you want cleaned
compare_file_for_names('COD_test.csv')
        
