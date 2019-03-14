#!/usr/bin/env python
import requests
import re

url = 'http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1'
line_len = 5

try:
	raw_file = requests.get(url).json()
except:
	print('Connection Error')
	exit()

content = re.sub(r'<.*?>', '',raw_file[0]['content'])
author = raw_file[0]['title']

words = content.split(' ')
lines = []
print(words)
while words != []:
	line = ' '.join(words[:line_len])
	words = words[line_len:]
	print(line)
	lines.append(line)

print(lines)


