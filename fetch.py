#!/usr/bin/env python
import html
import requests
import re

line_len = 5 #The maximum nomber of words in one line
url = 'http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1'
file_name = 'quote.txt'

try:
	raw_file = requests.get(url).json()
except:
	print('Connection Error')
	exit()

content = re.sub(r'<.*?>', '',raw_file[0]['content'])
content = html.unescape(content)
author = raw_file[0]['title']

words = content.split(' ')
lines = []

while words != []:
	line = ' '.join(words[:line_len])
	words = words[line_len:]
	lines.append(line)

file = open(file_name,'w')

for line in lines:
	file.write(line+'\n')



