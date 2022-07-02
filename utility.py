#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os.path
import re


if len(sys.argv) >= 3:
    if os.path.exists(sys.argv[2]):
        f = open(sys.argv[2], "r")
        file_content = f.read()
        if sys.argv[1] == '-c':
            total_line = len(open(sys.argv[2]).readlines(  ))
            print('Number of lines are:'+str(total_line))        
        elif sys.argv[1] == '-c':
            total_char = len(file_content)
            print('Number of lines are:'+str(total_char))
        elif sys.argv[1] == '-w':
            total_word = len(file_content.split())
            print('Number of lines are:'+str(total_word))
        elif sys.argv[1] == '-n':
            arr_match = re.findall('\d+', file_content) 
            final_str = ' '.join(arr_match)
            print(final_str)
        elif sys.argv[1] == '-a': 
            arr_match = re.findall('[a-z A-Z]', file_content) 
            final_str = ' '.join(arr_match)
            print(final_str)
    else:
        print('File not exists...')
else:
    print('Please enter the valid command line argument')
    print('eg. python3 utility.py -l test_file.txt')